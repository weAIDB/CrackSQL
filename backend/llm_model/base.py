# backend/llm_model/base.py
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Union
from langchain.schema import SystemMessage, HumanMessage


class BaseLLM(ABC):
    """Base LLM class"""

    def __init__(self, model_config: Dict[str, Any]):
        """
        Initialize LLM
        Args:
            model_config: Model configuration
        """
        self.model_config = model_config
        if not self.validate_config():  # No longer pass model_config parameter
            raise ValueError("Model configuration validation failed")

    @abstractmethod
    def validate_config(self) -> bool:  # Modify method signature, use instance variables
        """
        Validate model configuration
        Returns:
            bool: Whether the configuration is valid
        """
        pass

    @abstractmethod
    def chat(self,
                   messages: List[Union[SystemMessage, HumanMessage]],
                   **kwargs) -> str:
        """Chat interface"""
        pass

    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        """Generate text"""
        pass
