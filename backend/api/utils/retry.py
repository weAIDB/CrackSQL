from functools import wraps
import time
from config.logging_config import logger
from typing import Optional, Type, Union, Tuple

def retry_on_error(
    max_retries: int = 3,
    delay: int = 1,
    exceptions: Optional[Union[Type[Exception], Tuple[Type[Exception], ...]]] = None,
    logger_name: str = None
):
    """重试装饰器
    
    Args:
        max_retries: 最大重试次数
        delay: 重试延迟时间(秒)
        exceptions: 需要重试的异常类型，默认为所有异常
        logger_name: 日志记录器名称，用于自定义错误信息前缀
    
    Returns:
        装饰器函数
    
    Example:
        @retry_on_error(max_retries=3, delay=1, exceptions=(ValueError, KeyError))
        def my_function():
            pass
            
        @retry_on_error(logger_name="ChromaDB")
        def db_operation():
            pass
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            error_prefix = f"[{logger_name}] " if logger_name else ""
            
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    # 如果指定了异常类型，且当前异常不匹配，则直接抛出
                    if exceptions and not isinstance(e, exceptions):
                        raise
                        
                    if attempt == max_retries - 1:
                        logger.error(
                            f"{error_prefix}操作失败，已重试{max_retries}次: {str(e)}"
                        )
                        raise
                        
                    logger.warning(
                        f"{error_prefix}操作失败，正在重试 ({attempt + 1}/{max_retries}): {str(e)}"
                    )
                    # 使用指数退避策略
                    time.sleep(delay * (2 ** attempt))
            return None
        return wrapper
    return decorator 