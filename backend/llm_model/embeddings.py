# backend/llm_model/embeddings.py
from typing import List, Union
import numpy as np
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings
from tenacity import retry, stop_after_attempt, wait_random_exponential
from flask import current_app
from config.db_config import db, db_session_manager
from models import LLMModel
import logging

logger = logging.getLogger(__name__)


class CloudEmbedding:
    """云端Embedding实现"""

    def __init__(self, model_config: dict):
        self.embedding = OpenAIEmbeddings(
            model=model_config['name'],
            openai_api_key=model_config['api_key'],
            openai_api_base=model_config['api_base']
        )


class LocalEmbedding:
    """本地Embedding实现"""

    def __init__(self, model_config: dict):
        import torch

        # 确定设备
        device = "cuda" if torch.cuda.is_available() else "cpu"

        try:
            # 加载模型和分词器
            model_path = model_config['model_path']

            # 创建HuggingFaceEmbeddings实例，不再直接传入model和tokenizer
            self.embedding = HuggingFaceEmbeddings(
                model_name=model_path,
                model_kwargs={
                    'device': device,
                    'use_auth_token': None  # 避免token相关警告
                },
                encode_kwargs={
                    'normalize_embeddings': True,
                    'batch_size': 32,
                    'device': device
                },
                cache_folder=None  # 避免缓存相关警告
            )

            logger.info(f"成功初始化本地Embedding模型: {model_path}")

        except Exception as e:
            logger.error(f"加载本地Embedding模型失败: {str(e)}")
            raise


class EmbeddingManager:
    """Embedding管理器"""

    def __init__(self):
        self._embeddings = {}

    def get_embedding(self, model_name: str):
        """
        获取Embedding模型实例，如果不存在则加载
        Args:
            model_name: 模型名称
        Returns:
            Embedding模型实例
        """
        if model_name not in self._embeddings:
            # 懒加载：只在第一次使用时加载模型
            model_config = LLMModel.query.filter_by(
                name=model_name,
                category='embedding',
                is_active=True
            ).first()

            if not model_config:
                raise ValueError(f"Embedding模型不存在或未启用: {model_name}")

            self.load_embedding(model_config)

        return self._embeddings.get(model_name)

    def load_embedding(self, model_config: LLMModel):
        """
        加载单个Embedding模型
        Args:
            model_config: 模型配置
        """
        try:
            config_dict = {
                'name': model_config.name,
                'model_path': model_config.path,
                'api_base': model_config.api_base,
                'api_key': model_config.api_key
            }

            if model_config.deployment_type == 'cloud':
                # 云端模型
                embedding_instance = CloudEmbedding(config_dict)
                self._embeddings[model_config.name] = embedding_instance.embedding
            else:
                # 本地模型
                embedding_instance = LocalEmbedding(config_dict)
                self._embeddings[model_config.name] = embedding_instance.embedding

            logger.info(f"成功加载Embedding模型: {model_config.name}")

        except Exception as e:
            logger.error(f"加载Embedding模型失败 {model_config.name}: {str(e)}")
            raise

    def reload_embedding(self, model_name: str):
        """
        重新加载Embedding模型
        Args:
            model_name: 模型名称
        """
        # 移除旧的模型实例
        self._embeddings.pop(model_name, None)
        # 下次使用时会自动重新加载


# 全局Embedding管理器实例
embedding_manager = EmbeddingManager()


@retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(3))
@db_session_manager
async def get_embeddings(text: Union[str, List[str]], model_name: str) -> np.ndarray:
    """
    获取文本的embedding向量
    Args:
        text: 输入文本或文本列表
        model_name: 模型名称
    Returns:
        numpy.ndarray: 向量或向量列表
    """
    try:
        return await _get_embeddings_with_context(text, model_name)
    except Exception as e:
        logger.error(f"获取Embedding失败: {str(e)}")
        raise


async def _get_embeddings_with_context(text: Union[str, List[str]], model_name: str) -> np.ndarray:
    """在应用上下文中获取embedding向量"""
    # 获取模型实例
    embedding_model = embedding_manager.get_embedding(model_name)
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