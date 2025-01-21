# backend/llm_model/implementations.py
from typing import Dict, Any, List, Union
from .base import BaseLLM
from langchain.schema import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
import logging

logger = logging.getLogger(__name__)


class CloudLLM(BaseLLM):
    """云端LLM实现"""

    def __init__(self, model_config: Dict[str, Any]):
        super().__init__(model_config)  # 先调用父类构造函数
        self.llm = ChatOpenAI(
            model_name=self.model_config.get('name'),
            openai_api_key=self.model_config.get('api_key'),
            openai_api_base=self.model_config.get('api_base'),
            temperature=self.model_config.get('temperature', 0.7),
            max_tokens=self.model_config.get('max_tokens', 32000)
        )

    def validate_config(self) -> bool:
        """验证模型配置"""
        required_fields = ['name', 'api_key', 'api_base']
        for field in required_fields:
            if not self.model_config.get(field):
                raise ValueError(f"缺少必要的配置项: {field}")
        return True

    async def chat(self,
                   messages: List[Union[SystemMessage, HumanMessage]],
                   **kwargs) -> str:
        """使用LangChain的ChatOpenAI进行聊天"""
        try:
            # 使用 ainvoke 进行异步调用
            response = await self.llm.ainvoke(messages)
            return response.content
        except Exception as e:
            logger.error(f"Cloud LLM chat error: {str(e)}")
            raise

    async def generate(self, prompt: str, **kwargs) -> str:
        """生成文本"""
        try:
            messages = [HumanMessage(content=prompt)]
            # 使用 ainvoke 进行异步调用
            response = await self.llm.ainvoke(messages)
            return response.content
        except Exception as e:
            logger.error(f"Cloud LLM generate error: {str(e)}")
            raise


class LocalLLM(BaseLLM):
    """本地LLM实现"""

    def __init__(self, model_config: Dict[str, Any]):
        super().__init__(model_config)
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

        # 确定设备
        device = "cuda" if torch.cuda.is_available() else "cpu"

        try:
            # 加载模型和分词器
            model_path = self.model_config.get('model_path')
            model = AutoModelForCausalLM.from_pretrained(
                model_path,
                trust_remote_code=True,
                torch_dtype=torch.float16 if device == "cuda" else torch.float32
            ).to(device)

            tokenizer = AutoTokenizer.from_pretrained(
                model_path,
                trust_remote_code=True
            )

            # 创建pipeline
            pipe = pipeline(
                "text-generation",
                model=model,
                tokenizer=tokenizer,
                max_new_tokens=self.model_config.get('max_tokens', 2000),
                temperature=self.model_config.get('temperature', 0.7),
                device=device,
                return_full_text=False
            )

            # 创建LangChain包装器
            self.llm = HuggingFacePipeline(pipeline=pipe)

        except Exception as e:
            logger.error(f"加载本地模型失败: {str(e)}")
            raise

    def validate_config(self) -> bool:
        """验证模型配置"""
        if not self.model_config.get('model_path'):
            raise ValueError("缺少必要的配置项: model_path")
        return True

    async def chat(self,
                   messages: List[Union[SystemMessage, HumanMessage]],
                   **kwargs) -> str:
        """使用本地模型进行聊天"""
        try:
            # 将消息转换为模型可接受的格式
            prompt = self._format_messages(messages)
            # 生成响应
            response = await self.llm.agenerate([prompt])
            full_response = response.generations[0][0].text.strip()

            # 只提取 Assistant 的回复部分
            if "Assistant:" in full_response:
                assistant_response = full_response.split("Assistant:")[-1].strip()
            else:
                # 如果没有找到 Assistant: 标记，返回整个响应
                assistant_response = full_response

            logger.info(f"Local LLM chat response: {assistant_response}")
            print(f"Local LLM chat response: {assistant_response}")
            return response.generations[0][0].text.strip()
        except Exception as e:
            logger.error(f"Local LLM chat error: {str(e)}")
            raise

    async def generate(self, prompt: str, **kwargs) -> str:
        """生成文本"""
        try:
            response = await self.llm.agenerate([prompt])
            return response.generations[0][0].text.strip()
        except Exception as e:
            logger.error(f"Local LLM generate error: {str(e)}")
            raise

    def _format_messages(self, messages: List[Union[SystemMessage, HumanMessage]]) -> str:
        """格式化消息列表为单个提示词"""
        formatted_messages = []
        for msg in messages:
            if isinstance(msg, SystemMessage):
                formatted_messages.append(f"System: {msg.content}")
            elif isinstance(msg, HumanMessage):
                formatted_messages.append(f"Human: {msg.content}")
        return "\n".join(formatted_messages) + "\nAssistant:"


