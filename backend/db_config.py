from flask_sqlalchemy import SQLAlchemy
from config.logging_config import logger
from flask import current_app
from functools import wraps

db = SQLAlchemy()


def db_session_manager(func):
    """Database session manager decorator
    Ensure database operations are executed in the application context
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # 首先尝试获取当前应用上下文
            if not current_app:
                # 如果没有当前上下文，检查db.app是否已初始化
                if not hasattr(db, 'app') or db.app is None:
                    raise RuntimeError("数据库应用上下文未初始化，请确保先调用 create_app()")
                    
                with db.app.app_context():
                    return func(*args, **kwargs)
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"数据库操作失败: {str(e)}")
            # 重新抛出异常，保留原始的堆栈跟踪
            raise

    return wrapper 