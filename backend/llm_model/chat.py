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
    Chat completion interface
    Args:
        model_name: Model name
        messages: Message list, format: [{"role": "system/user", "content": "message content"}]
        stream: Whether to use streaming output
        **kwargs: Other parameters
    Returns:
        Dict[str, Any]: Return result
    """
    try:
        # Get model instance
        model = llm_manager.get_model(model_name)
        if not model:
            raise ValueError(f"Model {model_name} does not exist or is not enabled")

        # Convert message format
        formatted_messages = []
        for msg in messages:
            if msg["role"] == "system":
                formatted_messages.append(SystemMessage(content=msg["content"]))
            elif msg["role"] == "user":
                formatted_messages.append(HumanMessage(content=msg["content"]))
            else:
                logger.warning(f"Unknown message role: {msg['role']}")

        # Call model
        response = await model.chat(
            messages=formatted_messages,
            stream=stream,
            **kwargs
        )

        # Format return result
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
    Text generation interface
    Args:
        model_name: Model name
        prompt: Prompt
        stream: Whether to use streaming output
        **kwargs: Other parameters
    Returns:
        Dict[str, Any]: Return result
    """
    try:
        # Get model instance
        model = llm_manager.get_model(model_name)
        if not model:
            raise ValueError(f"Model {model_name} does not exist or is not enabled")

        # Call model
        response = await model.generate(
            prompt=prompt,
            stream=stream,
            **kwargs
        )

        # Format return result
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