# backend/llm_model/implementations.py

import json
import openai

import logging
from threading import Thread
from typing import Dict, Any, List, Union, AsyncGenerator
from langchain.schema import SystemMessage, HumanMessage

from cracksql.llm_model.base import BaseLLM

logger = logging.getLogger(__name__)


class CloudLLM(BaseLLM):
    """Cloud LLM implementation"""

    def __init__(self, model_config: Dict[str, Any]):
        super().__init__(model_config)  # Call parent constructor first
        # self.llm = ChatOpenAI(
        #     model_name=self.model_config.get('name'),
        #     openai_api_key=self.model_config.get('api_key'),
        #     openai_api_base=self.model_config.get('api_base'),
        #     temperature=self.model_config.get('temperature', 0.01),
        #     max_tokens=self.model_config.get('max_tokens', 32000)
        # )
        self.llm = openai.OpenAI(api_key=self.model_config.get('api_key'),
                                 base_url=self.model_config.get('api_base'))

    def validate_config(self) -> bool:
        """Validate model configuration"""
        required_fields = ['name', 'api_key', 'api_base']
        for field in required_fields:
            if not self.model_config.get(field):
                raise ValueError(f"Missing required configuration item: {field}")
        return True

    def chat(self, messages: List[Dict], **kwargs) -> str:
        try:
            # response = await self.llm.ainvoke(messages)
            # return response.content
            completion = self.llm.chat.completions.create(
                model=self.model_config.get('name'),
                messages=messages,
                max_tokens=self.model_config.get('max_tokens', 32000),
                temperature=self.model_config.get('temperature', 0.01)
            )
            response = json.loads(completion.to_json())
            response_format = {
                "role": response['choices'][0]['message']['role'],
                "content": response['choices'][0]['message']['content'],
                "raw": response
            }
            return response_format
        except Exception as e:
            logger.error(f"Cloud LLM chat error: {str(e)}")
            raise

    async def generate(self, prompt: str, **kwargs) -> str:
        """Generate text"""
        try:
            messages = [HumanMessage(content=prompt)]
            # Use ainvoke for asynchronous call
            response = await self.llm.ainvoke(messages)
            return response.content
        except Exception as e:
            logger.error(f"Cloud LLM generate error: {str(e)}")
            raise

    async def chat_stream(self,
                          messages: List[Union[SystemMessage, HumanMessage]],
                          **kwargs) -> AsyncGenerator[str, None]:
        """Stream chat using LangChain's ChatOpenAI"""
        logging.info(f"Local LLM chat stream prompt: {messages}")
        try:
            async for chunk in self.llm.astream(messages):
                if chunk.content:
                    yield chunk.content
        except Exception as e:
            logger.error(f"Cloud LLM chat stream error: {str(e)}")
            raise

    async def generate_stream(self, prompt: str, **kwargs) -> AsyncGenerator[str, None]:
        """Stream text generation"""
        try:
            messages = [HumanMessage(content=prompt)]
            async for chunk in self.llm.astream(messages):
                if chunk.content:
                    yield chunk.content
        except Exception as e:
            logger.error(f"Cloud LLM generate stream error: {str(e)}")
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
            self.model = AutoModelForCausalLM.from_pretrained(
                model_path,
                device_map="auto",  # Add device mapping
                trust_remote_code=True,
                torch_dtype=torch.bfloat16 if device == "cuda" else torch.float32,
                low_cpu_mem_usage=True,  # Reduce CPU memory usage
                attn_implementation="eager"  # Disable unstable optimizations
            ).to(device)

            self.tokenizer = AutoTokenizer.from_pretrained(
                model_path,
                trust_remote_code=True
            )

            # Save configuration
            self.device = device
            self.max_tokens = self.model_config.get('max_tokens', 2000)
            self.temperature = self.model_config.get('temperature', 0.01)
            self.streamer = TextIteratorStreamer(self.tokenizer)

            # Set model to evaluation mode
            self.model.eval()

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

    async def chat(self,
                   messages: List[Union[SystemMessage, HumanMessage]],
                   **kwargs) -> str:
        """Chat using local model"""
        try:
            # Convert messages to format acceptable by the model
            prompt = self._format_messages(messages)
            # Generate response
            response = await self.llm.agenerate([prompt])
            full_response = response.generations[0][0].text.strip()

            # Only extract the Assistant's reply part
            if "Assistant:" in full_response:
                assistant_response = full_response.split("Assistant:")[-1].strip()
            else:
                # If Assistant: marker not found, return the entire response
                assistant_response = full_response

            logger.info(f"Local LLM chat response: {assistant_response}")
            logging.info(f"Local LLM chat response: {assistant_response}")
            return response.generations[0][0].text.strip()
        except Exception as e:
            logger.error(f"Local LLM chat error: {str(e)}")
            raise

    async def generate(self, prompt: str, **kwargs) -> str:
        """Generate text"""
        try:
            response = await self.llm.agenerate([prompt])
            return response.generations[0][0].text.strip()
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

    async def chat_stream(self,
                          messages: List[Union[SystemMessage, HumanMessage]],
                          **kwargs) -> AsyncGenerator[str, None]:
        """Stream chat using local model"""
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

            # Update generation parameters
            generation_kwargs = dict(
                **inputs,  # Use inputs dictionary directly
                streamer=self.streamer,
                max_new_tokens=self.max_tokens,
                do_sample=True,
                temperature=self.temperature,
                top_p=0.9,  # Add top_p parameter
                pad_token_id=self.tokenizer.pad_token_id,
                eos_token_id=self.tokenizer.eos_token_id
            )

            thread = Thread(target=self.model.generate, kwargs=generation_kwargs)
            thread.start()

            for new_text in self.streamer:
                yield new_text.strip()
                # # Check if contains end marker
                # if "<|endoftext|>" in new_text:
                #     break
        except Exception as e:
            logger.error(f"Local LLM chat stream error: {str(e)}")
            raise

    async def generate_stream(self, prompt: str, **kwargs) -> AsyncGenerator[str, None]:
        """Stream text generation"""
        try:
            # Convert to chat format
            messages = [HumanMessage(content=prompt)]
            async for token in self.chat_stream(messages, **kwargs):
                yield token
        except Exception as e:
            logger.error(f"Local LLM generate stream error: {str(e)}")
            raise
