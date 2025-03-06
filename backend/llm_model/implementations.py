# backend/llm_model/implementations.py

import json
import openai
from threading import Thread
from typing import Dict, Any, List, Union, AsyncGenerator
from langchain.schema import SystemMessage, HumanMessage
from transformers import pipeline

from llm_model.base import BaseLLM
from config.logging_config import logger
from utils.constants import MAX_TOKENS_DEFAULT, TEMPERATURE_DEFAULT


class CloudLLM(BaseLLM):
    """Cloud LLM implementation"""

    def __init__(self, model_config: Dict[str, Any]):
        super().__init__(model_config)  # Call parent constructor first
        self.llm = openai.OpenAI(api_key=self.model_config.get('api_key'),
                                 base_url=self.model_config.get('api_base'))

    def validate_config(self) -> bool:
        """Validate model configuration"""
        required_fields = ['name', 'api_key', 'api_base']
        for field in required_fields:
            if not self.model_config.get(field):
                raise ValueError(f"Missing required configuration item: {field}")
        return True

    def chat(self, messages: List[Union[SystemMessage, HumanMessage]], **kwargs) -> str:
        """Chat with the model using OpenAI API"""
        import time
        import random

        max_retries = kwargs.get('max_retries', 5)
        base_delay = kwargs.get('base_delay', 3)  # 基础延迟时间（秒）

        # 将LangChain消息格式转换为OpenAI格式
        openai_messages = []
        for msg in messages:
            if isinstance(msg, SystemMessage):
                openai_messages.append({"role": "system", "content": msg.content})
            elif isinstance(msg, HumanMessage):
                openai_messages.append({"role": "user", "content": msg.content})
            elif isinstance(msg, dict):
                openai_messages.append(msg)
            else:
                openai_messages.append({"role": "assistant", "content": msg.content})

        # 重试机制
        for attempt in range(max_retries):
            try:
                # 添加随机延迟，避免请求过于集中
                if attempt > 0:
                    # 指数退避策略：随着重试次数增加，延迟时间指数增长
                    delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                    logger.info(
                        f"Rate limit reached, retrying in {delay:.2f} seconds (attempt {attempt + 1}/{max_retries})...")
                    time.sleep(delay)

                completion = self.llm.chat.completions.create(
                    model=self.model_config.get('name'),
                    messages=openai_messages,
                    max_tokens=self.model_config.get('max_tokens', MAX_TOKENS_DEFAULT),
                    temperature=self.model_config.get('temperature', TEMPERATURE_DEFAULT)
                )
                response = json.loads(completion.to_json())
                response_format = {
                    "role": response['choices'][0]['message']['role'],
                    "content": response['choices'][0]['message']['content'],
                    "raw": response
                }
                logger.info(f"Cloud LLM chat response: {response_format['content'][:100]}...")
                return response_format

            except openai.RateLimitError as e:
                logger.warning(f"Rate limit error (attempt {attempt + 1}/{max_retries}): {str(e)}")
                if attempt == max_retries - 1:  # 最后一次尝试
                    logger.error(f"Max retries reached. Cloud LLM chat error: {str(e)}")
                    raise
            except Exception as e:
                logger.error(f"Cloud LLM chat error: {str(e)}")
                raise

    def generate(self, prompt: str, **kwargs) -> str:
        """Generate text"""
        import time
        import random

        max_retries = kwargs.get('max_retries', 3)
        base_delay = kwargs.get('base_delay', 2)  # 基础延迟时间（秒）

        messages = [{"role": "user", "content": prompt}]

        # 重试机制
        for attempt in range(max_retries):
            try:
                # 添加随机延迟，避免请求过于集中
                if attempt > 0:
                    # 指数退避策略：随着重试次数增加，延迟时间指数增长
                    delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                    logger.info(
                        f"Rate limit reached, retrying in {delay:.2f} seconds (attempt {attempt + 1}/{max_retries})...")
                    time.sleep(delay)

                completion = self.llm.chat.completions.create(
                    model=self.model_config.get('name'),
                    messages=messages,
                    max_tokens=self.model_config.get('max_tokens', MAX_TOKENS_DEFAULT),
                    temperature=self.model_config.get('temperature', TEMPERATURE_DEFAULT)
                )
                response = json.loads(completion.to_json())
                response_format = {
                    "role": response['choices'][0]['message']['role'],
                    "content": response['choices'][0]['message']['content'],
                    "raw": response
                }
                logger.info(f"Cloud LLM generate response: {response_format['content'][:100]}...")
                return response_format

            except openai.RateLimitError as e:
                logger.warning(f"Rate limit error (attempt {attempt + 1}/{max_retries}): {str(e)}")
                if attempt == max_retries - 1:  # 最后一次尝试
                    logger.error(f"Max retries reached. Cloud LLM generate error: {str(e)}")
                    raise
            except Exception as e:
                logger.error(f"Cloud LLM generate error: {str(e)}")
                raise

    def release(self):
        """Release model resources"""
        # ChatOpenAI doesn't need special release operations
        pass


class LocalLLM(BaseLLM):
    """Local LLM implementation"""

    def __init__(self, model_config: Dict[str, Any]):
        super().__init__(model_config)
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
        # Determine device
        device = "cuda" if torch.cuda.is_available() else "cpu"

        try:
            # Load model and tokenizer
            model_path = self.model_config.get('model_path')
            self.model = pipeline(
                "text-generation",
                model=model_path,
                torch_dtype=torch.bfloat16,
                device_map="auto",
            )

            # Save configuration
            self.device = device
            self.max_tokens = self.model_config.get('max_tokens', MAX_TOKENS_DEFAULT)
            self.temperature = self.model_config.get('temperature', TEMPERATURE_DEFAULT)

        except Exception as e:
            logger.error(f"Failed to load local model: {str(e)}")
            raise

    def release(self):
        """Release model resources"""
        if hasattr(self, 'model'):
            # Release CUDA memory
            import torch
            if torch.cuda.is_available():
                torch.cuda.empty_cache()

            # Delete model reference
            del self.model
            self.model = None

        if hasattr(self, 'tokenizer'):
            del self.tokenizer
            self.tokenizer = None

    def validate_config(self) -> bool:
        """Validate model configuration"""
        if not self.model_config.get('model_path'):
            raise ValueError("Missing required configuration item: model_path")
        return True

    def chat(self,
             messages: List[Union[SystemMessage, HumanMessage]],
             **kwargs) -> str:
        """Chat using local model"""
        try:
            # Convert messages to format acceptable by the model
            prompt = self._format_messages(messages)

            full_response = self.model(
                messages,
                max_new_tokens=self.max_tokens,
            )
            assistant_response = full_response[0]["generated_text"][-1]
            # logger.info(f"Local LLM chat response: {assistant_response['content'][:100]}...")

            # 构造与CloudLLM相同的返回格式
            response_format = {
                "role": "assistant",
                "content": assistant_response['content'],
                "raw": {
                    "full_response": full_response,
                    "model": self.model_config.get('model_path'),
                    "prompt": prompt
                }
            }

            return response_format
        except Exception as e:
            logger.error(f"Local LLM chat error: {str(e)}")
            raise

    def generate(self, prompt: str, **kwargs) -> str:
        """Generate text"""
        try:
            # 使用本地模型生成响应
            inputs = self.tokenizer(
                prompt,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=self.max_tokens,
                return_attention_mask=True
            ).to(self.device)

            import torch
            with torch.no_grad():
                output = self.model.generate(
                    **inputs,
                    max_new_tokens=self.max_tokens,
                    do_sample=True,
                    temperature=self.temperature,
                    top_p=0.9,
                    pad_token_id=self.tokenizer.pad_token_id,
                    eos_token_id=self.tokenizer.eos_token_id
                )

            response_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
            logger.info(f"Local LLM generate response: {response_text[:100]}...")

            # 构造与CloudLLM相同的返回格式
            response_format = {
                "role": "assistant",
                "content": response_text,
                "raw": {
                    "full_response": response_text,
                    "model": self.model_config.get('model_path'),
                    "prompt": prompt
                }
            }

            return response_format
        except Exception as e:
            logger.error(f"Local LLM generate error: {str(e)}")
            raise

    def _format_messages(self, messages: List[Union[SystemMessage, HumanMessage]]) -> str:
        """Format message list into a single prompt"""
        formatted_messages = []
        for msg in messages:
            if isinstance(msg, dict):  # Handle dictionary format messages
                role = msg.get('role', '')
                content = msg.get('content', '')
                if role == 'system':
                    formatted_messages.append(f"System: {content}")
                elif role == 'user':
                    formatted_messages.append(f"Human: {content}")
                elif role == 'assistant':
                    formatted_messages.append(f"Assistant: {content}")
            else:  # Handle LangChain message objects
                if isinstance(msg, SystemMessage):
                    formatted_messages.append(f"System: {msg.content}")
                elif isinstance(msg, HumanMessage):
                    formatted_messages.append(f"Human: {msg.content}")
                else:
                    formatted_messages.append(f"Assistant: {msg.content}")

        # Ensure there's an Assistant: marker after the last message
        prompt = "\n".join(formatted_messages)
        if not prompt.rstrip().endswith("Assistant:"):
            prompt += "\nAssistant:"

        return prompt
