from typing import Dict, Optional
from .base import BaseLLM
from .implementations import CloudLLM, LocalLLM
from models import LLMModel
import logging

logger = logging.getLogger(__name__)


class LLMManager:
    """LLM模型管理器"""

    def __init__(self):
        self._models: Dict[str, BaseLLM] = {}

    def init_models(self):
        """初始化所有启用的模型"""
        try:
            # 获取所有启用的模型配置
            model_configs = LLMModel.query.filter_by(is_active=True).all()

            for config in model_configs:
                self.load_model(config)

        except Exception as e:
            logger.error(f"初始化模型失败: {str(e)}")
            raise

    def load_model(self, config: LLMModel) -> Optional[BaseLLM]:
        """
        加载单个模型
        Args:
            config: 模型配置
        Returns:
            Optional[BaseLLM]: 加载的模型实例
        """
        try:
            model_config = {
                'name': config.name,
                'deployment_type': config.deployment_type,
                'category': config.category,
                'temperature': config.temperature,
                'max_tokens': config.max_tokens,
                'model_path': config.path,
                'api_base': config.api_base,
                'api_key': config.api_key
            }

            # 根据类型创建相应的模型实例
            model_cls = CloudLLM if config.deployment_type == 'cloud' else LocalLLM
            model = model_cls(model_config)

            # 验证配置
            if not model.validate_config():
                logger.error(f"模型配置无效: {config.name}")
                return None

            self._models[config.name] = model
            logger.info(f"成功加载模型: {config.name}")
            return model

        except Exception as e:
            logger.error(f"加载模型失败 {config.name}: {str(e)}")
            return None

    def get_model(self, name: str) -> Optional[BaseLLM]:
        """获取模型实例"""
        if name not in self._models:
            # 懒加载：只在第一次使用时加载模型
            config = LLMModel.query.filter_by(name=name).first()
            if not config:
                logger.error(f"模型配置不存在: {name}")
                return None
            self.load_model(config)
        return self._models.get(name)

    def reload_model(self, name: str) -> Optional[BaseLLM]:
        """重新加载模型"""
        try:
            config = LLMModel.query.filter_by(name=name).first()
            if not config:
                logger.error(f"模型配置不存在: {name}")
                return None

            # 移除旧的模型实例
            self._models.pop(name, None)

            # 加载新的模型实例
            return self.load_model(config)

        except Exception as e:
            logger.error(f"重新加载模型失败 {name}: {str(e)}")
            return None


# 全局LLM管理器实例
llm_manager = LLMManager()
