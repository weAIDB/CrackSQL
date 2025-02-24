from typing import List, Union
import numpy as np
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings
from tenacity import retry, stop_after_attempt, wait_random_exponential
from config.db_config import db, db_session_manager
from models import LLMModel
import logging
from typing import Optional, Dict

logger = logging.getLogger(__name__)


class EmbeddingManager:
    """Embedding管理器"""

    def __init__(self):
        self._embeddings = {}

    @db_session_manager
    def get_embedding_config_from_db(self, model_name: str):
        """
        获取Embedding模型配置
        """
        config = db.session.query(LLMModel).filter_by(name=model_name, category='embedding', is_active=True).first()
        return {
            'name': config.name,
            'model_path': config.path,
            'api_base': config.api_base,
            'api_key': config.api_key,
            'deployment_type': config.deployment_type,
            'dimension': config.dimension
        }
    
    def release_embedding(self, model_name: str):
        """释放Embedding模型"""
        if model_name in self._embeddings:
            embedding_model = self._embeddings[model_name]
            try:
                # 对于HuggingFace模型，需要释放CUDA内存
                if isinstance(embedding_model, HuggingFaceEmbeddings):
                    import torch
                    if torch.cuda.is_available():
                        torch.cuda.empty_cache()
                    if hasattr(embedding_model, 'client'):
                        del embedding_model.client
                
                # OpenAI模型不需要特别的释放操作
                del self._embeddings[model_name]
                
            except Exception as e:
                logger.error(f"释放Embedding模型 {model_name} 失败: {str(e)}")

    def release_all_embeddings(self):
        """释放所有Embedding模型"""
        model_names = list(self._embeddings.keys())  # 创建副本避免在迭代时修改字典
        for model_name in model_names:
            self.release_embedding(model_name)


    def get_embedding(self, model_name: str, model_config: Optional[Dict] = None):
        """
        获取Embedding模型实例，如果不存在则加载
        Args:
            model_name: 模型名称
            model_config: 模型配置
        Returns:
            Embedding模型实例
        """
        if model_name not in self._embeddings:
            # 懒加载：只在第一次使用时加载模型
            if model_config is None:
                model_config = self.get_embedding_config_from_db(model_name)
                if not model_config:
                    raise ValueError(f"Embedding模型不存在或未启用: {model_name}")
            self.load_embedding(model_config)

        return self._embeddings.get(model_name)

    def load_embedding(self, model_config: dict):
        """
        加载单个Embedding模型
        Args:
            model_config: 模型配置
        """
        try:
            if model_config['deployment_type'] == 'cloud':
                # 云端模型（OpenAI）
                embedding = OpenAIEmbeddings(
                    model=model_config['name'],
                    openai_api_key=model_config['api_key'],
                    openai_api_base=model_config['api_base']
                )
            else:
                import torch
                # 确定设备
                device = "cuda" if torch.cuda.is_available() else "cpu"
                # 本地模型（HuggingFace）
                embedding = HuggingFaceEmbeddings(
                    model_name=model_config['model_path'],
                    model_kwargs={'device': device},
                    encode_kwargs={'normalize_embeddings': True}
                )
            self._embeddings[model_config['name']] = embedding
            logger.info(f"成功加载Embedding模型: {model_config['name']}")
        except Exception as e:
            logger.error(f"加载Embedding模型失败 {model_config['name']}: {str(e)}")
            raise


# 全局Embedding管理器实例
embedding_manager = EmbeddingManager()


@retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(3))
async def get_embeddings(text: Union[str, List[str]], model_name: str,
                         model_config: Optional[Dict] = None) -> np.ndarray:
    """
    获取文本的embedding向量
    Args:
        text: 输入文本或文本列表
        model_name: 模型名称
    Returns:
        numpy.ndarray: 向量或向量列表
    """
    try:
        return await _get_embeddings_with_context(text, model_name, model_config=model_config)
    except Exception as e:
        logger.error(f"获取Embedding失败: {str(e)}")
        raise


async def _get_embeddings_with_context(text: Union[str, List[str]], model_name: str,
                                       model_config: Optional[Dict] = None) -> np.ndarray:
    """在应用上下文中获取embedding向量"""
    # 获取模型实例
    embedding_model = embedding_manager.get_embedding(model_name, model_config)
    if not embedding_model:
        raise ValueError(f"Embedding模型不存在或未启用: {model_name}")
    try:
        # 使用LangChain的embed_query/embed_documents方法
        if isinstance(text, str):
            embedding = await embedding_model.aembed_query(text)
        else:
            embedding = await embedding_model.aembed_documents(text)
        return np.array(embedding)
    except Exception as e:
        logger.error(f"生成Embedding失败: {str(e)}")
        raise
