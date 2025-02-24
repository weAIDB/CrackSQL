# backend/llm_model/implementations.py
from typing import Dict, Any, List, Union, AsyncGenerator
from .base import BaseLLM
from langchain.schema import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
import logging
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from threading import Thread

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

    async def chat_stream(self,
                          messages: List[Union[SystemMessage, HumanMessage]],
                          **kwargs) -> AsyncGenerator[str, None]:
        """使用LangChain的ChatOpenAI进行流式聊天"""
        print(f"Local LLM chat stream prompt: {messages}")
        try:
            async for chunk in self.llm.astream(messages):
                if chunk.content:
                    yield chunk.content
        except Exception as e:
            logger.error(f"Cloud LLM chat stream error: {str(e)}")
            raise

    async def generate_stream(self, prompt: str, **kwargs) -> AsyncGenerator[str, None]:
        """流式生成文本"""
        try:
            messages = [HumanMessage(content=prompt)]
            async for chunk in self.llm.astream(messages):
                if chunk.content:
                    yield chunk.content
        except Exception as e:
            logger.error(f"Cloud LLM generate stream error: {str(e)}")
            raise
    
    def release(self):
        """释放模型资源"""
        # ChatOpenAI 不需要特别的释放操作
        pass


class LocalLLM(BaseLLM):
    """本地LLM实现"""

    def __init__(self, model_config: Dict[str, Any]):
        super().__init__(model_config)
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
        # 确定设备
        device = "cuda" if torch.cuda.is_available() else "cpu"

        try:
            # 加载模型和分词器
            model_path = self.model_config.get('model_path')
            self.model = AutoModelForCausalLM.from_pretrained(
                model_path,
                device_map="auto",  # 添加设备映射
                trust_remote_code=True,
                torch_dtype=torch.bfloat16 if device == "cuda" else torch.float32,
                low_cpu_mem_usage=True,  # 减少CPU内存使用
                attn_implementation="eager"  # 禁用不稳定优化
            ).to(device)

            self.tokenizer = AutoTokenizer.from_pretrained(
                model_path,
                trust_remote_code=True
            )

            # 保存配置
            self.device = device
            self.max_tokens = self.model_config.get('max_tokens', 2000)
            self.temperature = self.model_config.get('temperature', 0.7)
            self.streamer = TextIteratorStreamer(self.tokenizer)

            # 设置模型为评估模式
            self.model.eval()

        except Exception as e:
            logger.error(f"加载本地模型失败: {str(e)}")
            raise
    
    def release(self):
        """释放模型资源"""
        if hasattr(self, 'model'):
            # 释放 CUDA 内存
            import torch
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            
            # 删除模型引用
            del self.model
            self.model = None
            
        if hasattr(self, 'tokenizer'):
            del self.tokenizer
            self.tokenizer = None

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
            if isinstance(msg, dict):  # 处理字典格式的消息
                role = msg.get('role', '')
                content = msg.get('content', '')
                if role == 'system':
                    formatted_messages.append(f"System: {content}")
                elif role == 'user':
                    formatted_messages.append(f"Human: {content}")
                elif role == 'assistant':
                    formatted_messages.append(f"Assistant: {content}")
            else:  # 处理 LangChain 消息对象
                if isinstance(msg, SystemMessage):
                    formatted_messages.append(f"System: {msg.content}")
                elif isinstance(msg, HumanMessage):
                    formatted_messages.append(f"Human: {msg.content}")
                else:
                    formatted_messages.append(f"Assistant: {msg.content}")

        # 确保最后一条消息后有 Assistant: 标记
        prompt = "\n".join(formatted_messages)
        if not prompt.rstrip().endswith("Assistant:"):
            prompt += "\nAssistant:"

        return prompt

    async def chat_stream(self,
                          messages: List[Union[SystemMessage, HumanMessage]],
                          **kwargs) -> AsyncGenerator[str, None]:
        """使用本地模型进行流式聊天"""
        try:
            prompt = self._format_messages(messages)

            inputs = self.tokenizer(
                prompt,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=self.max_tokens,
                return_attention_mask=True
            ).to(self.device)

            # 更新生成参数
            generation_kwargs = dict(
                **inputs,  # 直接使用inputs字典
                streamer=self.streamer,
                max_new_tokens=self.max_tokens,
                do_sample=True,
                temperature=self.temperature,
                top_p=0.9,  # 添加top_p参数
                pad_token_id=self.tokenizer.pad_token_id,
                eos_token_id=self.tokenizer.eos_token_id
            )

            thread = Thread(target=self.model.generate, kwargs=generation_kwargs)
            thread.start()

            found_assistant = False
            current_response = ""

            for new_text in self.streamer:
                print("======:", new_text)
                yield new_text.strip()
                # # 检查是否包含结束标记
                # if "<|endoftext|>" in new_text:
                #     break
                #
                # if new_text:
                #     if not found_assistant:
                #         if "Assistant:" in new_text:
                #             found_assistant = True
                #             _, response = new_text.split("Assistant:", 1)
                #             if response.strip():
                #                 current_response = response.strip()
                #                 print(f"AI: {current_response}")  # 打印首次回复
                #                 yield current_response
                #     else:
                #         # 检查新文本是否是之前响应的重复
                #         if new_text.strip() not in current_response:
                #             current_response = new_text.strip()
                #             print(f"AI: {new_text.strip()}")  # 打印后续回复
                #             yield new_text.strip()

            thread.join()

        except Exception as e:
            logger.error(f"Local LLM chat stream error: {str(e)}")
            raise

    async def generate_stream(self, prompt: str, **kwargs) -> AsyncGenerator[str, None]:
        """流式生成文本"""
        try:
            # 使用 tokenizer 处理输入，获取 input_ids 和 attention_mask
            inputs = self.tokenizer(
                prompt,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=self.max_tokens,
                return_attention_mask=True
            ).to(self.device)

            # 创建生成参数
            generation_kwargs = dict(
                input_ids=inputs["input_ids"],
                attention_mask=inputs["attention_mask"],  # 添加 attention_mask
                max_new_tokens=self.max_tokens,
                temperature=self.temperature,
                streamer=self.streamer,
                pad_token_id=self.tokenizer.pad_token_id,
                eos_token_id=self.tokenizer.eos_token_id,  # 添加 eos_token_id
                do_sample=True,  # 启用采样
            )

            # 在后台线程中运行模型生成
            thread = Thread(target=self.model.generate, kwargs=generation_kwargs)
            thread.start()

            # 从streamer中获取生成的文本
            for new_text in self.streamer:
                if new_text:
                    yield new_text.strip()

            thread.join()  # 等待生成完成

        except Exception as e:
            logger.error(f"Local LLM generate stream error: {str(e)}")
            raise


