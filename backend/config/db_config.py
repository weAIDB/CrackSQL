from flask_sqlalchemy import SQLAlchemy
from config.logging_config import logger
from flask import current_app
from functools import wraps

db = SQLAlchemy()


def db_session_manager(func):
    """数据库会话管理装饰器
    确保在应用上下文中执行数据库操作
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # 确保在应用上下文中运行
            if not current_app:
                with db.app.app_context():
                    return func(*args, **kwargs)
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"数据库操作失败: {str(e)}")
            raise

    return wrapper

#  flask_migrate 使用
#  flask db init  初始化
#  flask db migrate  生成版本文件
#  flask db upgrade  同步到数据库
