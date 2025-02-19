import chromadb
from chromadb.config import Settings
from typing import List, Dict, Optional, Any
import os
from config.logging_config import logger
from config.cache import cache
from api.utils.retry import retry_on_error
import time
import hashlib
import re


def convert_distance_to_score(distance: float) -> float:
    """
    将Chroma的距离值转换为0-100的相似度分数
    Chroma使用cosine distance (1 - cosine_similarity)
    distance = 0 表示完全相同，distance = 2 表示完全相反
    我们将其转换为：0 表示完全不同，100 表示完全相同
    """

    if distance is None:
        return 0
    # 将distance从[0,2]映射到[0,100]
    score = (1 - distance / 2) * 100
    # 小数点后两位
    score = round(score, 2)
    # 确保分数在0-100范围内
    return max(0, min(100, score))


def generate_kb_name(kb_name: str) -> str:
    """生成知识库名称
    Args:
        kb_name: 知识库名称
        
    Returns:
        str: 合法的表名
    """
    # 使用 MD5 对中文名称进行哈希，保证表名唯一性
    name_hash = hashlib.md5(kb_name.encode('utf-8')).hexdigest()[:8]
    # 移除所有非字母数字字符，转换为小写
    safe_name = re.sub(r'[^a-zA-Z0-9]', '_', kb_name.encode('ascii', 'ignore').decode('ascii').lower())
    # 组合表名：前缀 + 安全名称 + 哈希值
    return f"vector_store_{safe_name}_{name_hash}"


class ChromaStore:
    """Chroma向量存储管理器"""

    def __init__(self, persist_directory: str = "./instance/chroma"):
        """
        初始化ChromaStore
        
        Args:
            persist_directory: 持久化目录
        """
        self.persist_directory = persist_directory
        os.makedirs(persist_directory, exist_ok=True)

        # 配置Chroma客户端
        self.client = chromadb.PersistentClient(
            path=persist_directory,
            settings=Settings(
                anonymized_telemetry=False,  # 关闭遥测
                allow_reset=True,
                is_persistent=True
            )
        )

    def _get_collection(self, collection_id: str):
        """获取集合"""
        return self.client.get_collection(
            name=collection_id,
            embedding_function=None
        )

    @retry_on_error(logger_name="ChromaDB")
    def get_collection_by_id(self, collection_id: str):
        """通过ID获取集合"""
        return self._get_collection(collection_id)

    @retry_on_error(logger_name="ChromaDB")
    def get_or_create_collection(self, kb_name: str, dimension: int = 1536) -> str:
        """获取或创建集合
        
        Args:
            kb_name: 知识库名称
            dimension: 向量维度
            
        Returns:
            str: 集合ID
        """
        kb_name = generate_kb_name(kb_name)
        try:
            # 先尝试获取已存在的集合
            try:
                collection = self.client.get_collection(
                    name=kb_name,
                    embedding_function=None
                )
                logger.info(f"获取已存在的集合: {kb_name}")
                return kb_name
            except Exception:
                # 如果集合不存在，创建新集合
                metadata = {
                    "hnsw:space": "cosine",
                    "dimension": str(dimension),
                    "hnsw:search_ef": 200,
                    "hnsw:construction_ef": 200,
                    "hnsw:M": 32
                }

                collection = self.client.create_collection(
                    name=kb_name,
                    embedding_function=None,
                    metadata=metadata
                )
                logger.info(f"创建新集合: {kb_name}")

            return kb_name
        except Exception as e:
            logger.error(f"创建集合失败: {str(e)}")
            raise

    def _validate_inputs(self, texts: List[str], embeddings: List[List[float]], ids: Optional[List[str]] = None):
        """验证输入数据的一致性"""
        if len(texts) != len(embeddings):
            raise ValueError("文本数量与向量数量不匹配")
        if ids and len(ids) != len(texts):
            raise ValueError("ID数量与文本数量不匹配")

    @retry_on_error(logger_name="ChromaDB")
    def add_texts(
            self,
            collection_id: str,
            texts: List[str],
            embeddings: List[List[float]],
            metadatas: Optional[List[Dict]] = None,
            ids: Optional[List[str]] = None,
            batch_size: int = 100
    ):
        """添加文本到向量库"""
        self._validate_inputs(texts, embeddings, ids)
        collection = self._get_collection(collection_id)

        if not ids:
            existing_count = collection.count()
            ids = [str(i) for i in range(existing_count, existing_count + len(texts))]

        # 分批添加，避免内存溢出
        for i in range(0, len(texts), batch_size):
            end_idx = min(i + batch_size, len(texts))
            collection.add(
                embeddings=embeddings[i:end_idx],
                documents=texts[i:end_idx],
                metadatas=metadatas[i:end_idx] if metadatas else None,
                ids=ids[i:end_idx]
            )

    @retry_on_error(logger_name="ChromaDB")
    def search_by_id(
            self,
            collection_id: str,
            query_embedding: List[float],
            top_k: int = 5,
            where: Optional[Dict] = None,
            where_document: Optional[Dict] = None,
            **kwargs
    ) -> List[Dict]:
        """通过集合ID搜索"""
        collection = self._get_collection(collection_id)

        try:
            results = collection.query(
                query_embeddings=query_embedding.tolist(),
                n_results=top_k,
                where=where,
                include=["documents", "metadatas", "distances"],
                where_document=where_document,
                **kwargs
            )

            return [
                {
                    'content': doc,
                    'metadata': meta if meta else {},
                    'score': convert_distance_to_score(distance),
                    'id': id_
                }
                for doc, meta, distance, id_ in zip(
                    results['documents'][0],
                    results['metadatas'][0] if results['metadatas'] else [None] * len(results['documents'][0]),
                    results['distances'][0] if results['distances'] else [None] * len(results['documents'][0]),
                    results['ids'][0]
                )
            ]
        except Exception as e:
            logger.error(f"搜索失败: {str(e)}")
            raise

    @retry_on_error(logger_name="ChromaDB")
    def delete_by_ids(self, collection_id: str, ids: List[str]):
        """通过ID删除向量"""
        collection = self._get_collection(collection_id)
        try:
            collection.delete(ids=ids)
        except Exception as e:
            logger.error(f"删除向量失败: {str(e)}")
            raise

    @retry_on_error(logger_name="ChromaDB")
    def update_texts(
            self,
            collection_id: str,
            texts: List[str],
            embeddings: List[List[float]],
            ids: List[str],
            metadatas: Optional[List[Dict]] = None
    ):
        """更新向量"""
        self._validate_inputs(texts, embeddings, ids)
        collection = self._get_collection(collection_id)
        try:
            collection.update(
                ids=ids,
                embeddings=embeddings,
                documents=texts,
                metadatas=metadatas
            )
        except Exception as e:
            logger.error(f"更新向量失败: {str(e)}")
            raise

    @retry_on_error(logger_name="ChromaDB")
    def delete_collection(self, collection_id: str):
        """删除集合"""
        try:
            self.client.delete_collection(collection_id)
        except Exception as e:
            logger.error(f"删除集合失败: {str(e)}")
            raise

    @cache.memoize(timeout=60)  # 1分钟缓存
    def get_collection_stats(self, collection_id: str) -> Dict[str, Any]:
        """获取集合统计信息"""
        collection = self._get_collection(collection_id)
        try:
            return {
                'total_count': collection.count(),
                'name': collection.name,
                'metadata': collection.metadata,
                'last_updated': time.time()
            }
        except Exception as e:
            logger.error(f"获取集合统计信息失败: {str(e)}")
            raise
