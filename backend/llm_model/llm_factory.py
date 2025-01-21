from typing import Optional
from models import LLMModel
from .base import BaseLLM
from .implementations import LocalLLM, CloudLLM

class LLMFactory:
    """LLM工厂类"""
    
    @staticmethod
    def get_llm(model_name: str) -> Optional[BaseLLM]:
        """获取LLM实例"""
        # 获取模型配置
        model = LLMModel.query.filter_by(name=model_name, is_active=True).first()
        if not model:
            raise ValueError(f"模型 {model_name} 不存在或未启用")
            
        # 根据部署类型创建实例
        if model.deployment_type == 'local':
            return LocalLLM(model)
        elif model.deployment_type == 'cloud':
            return CloudLLM(model)
        else:
            raise ValueError(f"不支持的部署类型: {model.deployment_type}")

def get_llm(model_name: str) -> BaseLLM:
    """获取LLM实例的便捷方法"""
    return LLMFactory.get_llm(model_name) 