from typing import Dict, Optional
from .base import BaseLLM
from .implementations import CloudLLM, LocalLLM
from models import LLMModel
import logging
from config.db_config import db_session_manager


logger = logging.getLogger(__name__)


class LLMManager:
    """LLM模型管理器"""

    def __init__(self):
        self._models: Dict[str, BaseLLM] = {}

    def load_model(self, model_config: Dict) -> Optional[BaseLLM]:
        """
        加载单个模型
        Args:
            config: 模型配置
        Returns:
            Optional[BaseLLM]: 加载的模型实例
        """
        try:
            # 根据类型创建相应的模型实例
            model_cls = CloudLLM if model_config['deployment_type'] == 'cloud' else LocalLLM
            model = model_cls(model_config)

            # 验证配置
            if not model.validate_config():
                logger.error(f"模型配置无效: {model_config['name']}")
                return None

            self._models[model_config['name']] = model
            logger.info(f"成功加载模型: {model_config['name']}")
            return model

        except Exception as e:
            logger.error(f"加载模型失败 {model_config['name']}: {str(e)}")
            return None
    

    @db_session_manager
    def get_model_config_from_db(self, name: str) -> Optional[Dict]:
        """从数据库获取模型配置"""
        config = LLMModel.query.filter_by(name=name).first()
        if not config:
            logger.error(f"模型配置不存在: {name}")
            return None
        if not config.is_active:
            logger.error(f"模型未启用: {name}")
            return None

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

        return model_config


    def reload_model(self, name: str, config: Optional[Dict] = None) -> Optional[BaseLLM]:
        """
        重新加载模型
        Args:
            name: 模型名称
            config: 可选的模型配置字典
        Returns:
            Optional[BaseLLM]: 重新加载的模型实例
        """
        if name not in self._models:
            logger.error(f"模型不存在: {name}, 不需要重新加载")

        # 释放模型，释放后模型会被销毁
        # self._models[name].release()

        # 重新加载模型
        return self.get_model(name, config)


    def get_model(self, name: str, config: Optional[Dict] = None) -> Optional[BaseLLM]:
        """获取模型实例
        Args:
            name: 模型名称
            config: 可选的模型配置字典
        Returns:
            Optional[BaseLLM]: 模型实例
        """
        if name not in self._models:
            if config is None:
                config = self.get_model_config_from_db(name)
                if not config:
                    logger.error(f"模型配置不存在: {name}")
                    return None
            else:
                # 使用字典访问方式
                if config['deployment_type'] == 'cloud' and (config.get('api_base') is None or config.get('api_key') is None):
                    logger.error(f"模型配置参数不全: {config['name']}")
                    return None
                elif config['deployment_type'] == 'local' and config.get('model_path') is None:
                    logger.error(f"模型配置参数不全: {config['name']}")
                    return None
            return self.load_model(config)
        return self._models.get(name)


# 全局LLM管理器实例
llm_manager = LLMManager()
