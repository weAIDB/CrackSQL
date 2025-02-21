import chromadb
from chromadb.config import Settings
from typing import List, Dict, Optional, Any
import os
from config.logging_config import logger
from chromadb.api.models.Collection import Collection
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


def generate_collection_id(kb_name: str, content_type: str) -> str:
    """生成集合ID
    Args:
        kb_name: 知识库名称
        content_type: 内容类型
        
    Returns:
        str: 合法的表名
    """
    # 使用 MD5 对中文名称进行哈希，保证表名唯一性
    name_hash = hashlib.md5(kb_name.encode('utf-8')).hexdigest()[:8]
    # 移除所有非字母数字字符，转换为小写
    safe_name = re.sub(r'[^a-zA-Z0-9]', '_', kb_name.encode('ascii', 'ignore').decode('ascii').lower())
    # 组合表名：前缀 + 安全名称 + 哈希值
    return f"vector_store_{safe_name}_{name_hash}_{content_type}"


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
        try:
            return self.client.get_collection(
                name=collection_id,
                embedding_function=None
            )
        except Exception as e:
            logger.error(f"获取集合失败: {str(e)}")
            return None

    @retry_on_error(logger_name="ChromaDB")
    def get_or_create_collection(self, collection_id: str, dimension: int = 1536) -> Collection:
        """获取或创建集合
        
        Args:
            collection_id: 集合ID
            dimension: 向量维度
            
        Returns:
            str: 集合ID
        """
        try:
            # 先尝试获取已存在的集合
            try:
                collection = self.client.get_collection(
                    name=collection_id,
                    embedding_function=None
                )
                logger.info(f"获取已存在的集合: {collection_id}")
                return collection
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
                    name=collection_id,
                    embedding_function=None,
                    metadata=metadata
                )
                logger.info(f"创建新集合: {collection_id}")

                return collection
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
            kb_name: str,
            content_type: str,
            texts: List[str],
            embeddings: List[List[float]],
            metadatas: Optional[List[Dict]] = None,
            ids: Optional[List[str]] = None,
            batch_size: int = 100
    ):
        """添加文本到向量库"""
        self._validate_inputs(texts, embeddings, ids)
        collection_id = generate_collection_id(kb_name, content_type)
        collection = self.get_or_create_collection(collection_id)

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
    def search(
            self,
            kb_name: str,
            query_embedding: List[float],
            content_type: str = None,
            top_k: int = 5,
            where: Optional[Dict] = None,
            where_document: Optional[Dict] = None,
            **kwargs
    ) -> List[Dict]:
        """通过知识库名称和内容类型搜索"""

        collection_ids = []

        if not content_type:
            # 获取所有内容类型
            content_types = ['function', 'keyword', 'type', 'operator']
            for content_type in content_types:
                collection_ids.append(generate_collection_id(kb_name, content_type))
        else:
            collection_ids.append(generate_collection_id(kb_name, content_type))

        results_all = []
        for collection_id in collection_ids:
            collection = self._get_collection(collection_id)
            if not collection:
                continue
            try:
                results = collection.query(
                    query_embeddings=[query_embedding],
                    n_results=top_k,
                    where=where,
                    include=["documents", "metadatas", "distances"],
                    where_document=where_document,
                    **kwargs
                )
                results_all.extend([
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
                ])
            except Exception as e:
                logger.error(f"搜索失败: {str(e)}")
                raise
        
        # 根据score排序
        results_all.sort(key=lambda x: x['score'], reverse=True)

        return results_all

    @retry_on_error(logger_name="ChromaDB")
    def delete_by_ids(self, kb_name: str, content_type: str, ids: List[str]):
        """通过ID删除向量"""
        collection_id = generate_collection_id(kb_name, content_type)
        collection = self._get_collection(collection_id)
        if not collection:
            return
        try:
            collection.delete(ids=ids)
        except Exception as e:
            logger.error(f"删除向量失败: {str(e)}")
            raise

    @retry_on_error(logger_name="ChromaDB")
    def delete_collection(self, kb_name: str):
        """删除集合"""
        try:
            for content_type in ['function', 'keyword', 'type', 'operator']:
                self.client.delete_collection(generate_collection_id(kb_name, content_type))
        except Exception as e:
            logger.error(f"删除集合失败: {str(e)}")
