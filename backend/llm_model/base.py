# backend/llm_model/base.py
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Union
from langchain.schema import SystemMessage, HumanMessage
import logging

logger = logging.getLogger(__name__)


class BaseLLM(ABC):
    """基础LLM类"""

    def __init__(self, model_config: Dict[str, Any]):
        """
        初始化LLM
        Args:
            model_config: 模型配置
        """
        self.model_config = model_config
        if not self.validate_config():  # 不再传递 model_config 参数
            raise ValueError("模型配置验证失败")

    @abstractmethod
    def validate_config(self) -> bool:  # 修改方法签名，使用实例变量
        """
        验证模型配置
        Returns:
            bool: 配置是否有效
        """
        pass

    @abstractmethod
    async def chat(self,
                   messages: List[Union[SystemMessage, HumanMessage]],
                   **kwargs) -> str:
        """聊天接口"""
        pass

    @abstractmethod
    async def generate(self, prompt: str, **kwargs) -> str:
        """生成文本"""
        pass
