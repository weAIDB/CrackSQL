from typing import List, Dict, Any
from langchain.schema import SystemMessage, HumanMessage
from .llm_manager import llm_manager
import logging

logger = logging.getLogger(__name__)


async def chat_completion(
        model_name: str,
        messages: List[Dict[str, str]],
        stream: bool = False,
        **kwargs
) -> Dict[str, Any]:
    """
    聊天完成接口
    Args:
        model_name: 模型名称
        messages: 消息列表，格式为[{"role": "system/user", "content": "消息内容"}]
        stream: 是否使用流式输出
        **kwargs: 其他参数
    Returns:
        Dict[str, Any]: 返回结果
    """
    try:
        # 获取模型实例
        model = llm_manager.get_model(model_name)
        if not model:
            raise ValueError(f"模型 {model_name} 不存在或未启用")

        # 转换消息格式
        formatted_messages = []
        for msg in messages:
            if msg["role"] == "system":
                formatted_messages.append(SystemMessage(content=msg["content"]))
            elif msg["role"] == "user":
                formatted_messages.append(HumanMessage(content=msg["content"]))
            else:
                logger.warning(f"未知的消息角色: {msg['role']}")

        # 调用模型
        response = await model.chat(
            messages=formatted_messages,
            stream=stream,
            **kwargs
        )

        # 格式化返回结果
        if stream:
            return {
                "status": "success",
                "response": response,
                "is_stream": True
            }

        return {
            "status": "success",
            "response": response,
            "is_stream": False
        }

    except Exception as e:
        logger.error(f"Chat completion error: {str(e)}")
        return {
            "status": "error",
            "error": str(e),
            "is_stream": False
        }


async def generate_text(
        model_name: str,
        prompt: str,
        stream: bool = False,
        **kwargs
) -> Dict[str, Any]:
    """
    文本生成接口
    Args:
        model_name: 模型名称
        prompt: 提示词
        stream: 是否使用流式输出
        **kwargs: 其他参数
    Returns:
        Dict[str, Any]: 返回结果
    """
    try:
        # 获取模型实例
        model = llm_manager.get_model(model_name)
        if not model:
            raise ValueError(f"模型 {model_name} 不存在或未启用")

        # 调用模型
        response = await model.generate(
            prompt=prompt,
            stream=stream,
            **kwargs
        )

        # 格式化返回结果
        if stream:
            return {
                "status": "success",
                "response": response,
                "is_stream": True
            }

        return {
            "status": "success",
            "response": response,
            "is_stream": False
        }

    except Exception as e:
        logger.error(f"Text generation error: {str(e)}")
        return {
            "status": "error",
            "error": str(e),
            "is_stream": False
        }