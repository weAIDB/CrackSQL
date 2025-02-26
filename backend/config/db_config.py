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
            # Ensure the operation is performed in the application context
            if not current_app:
                with db.app.app_context():
                    return func(*args, **kwargs)
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Database operation failed: {str(e)}")
            raise

    return wrapper

#  flask_migrate Usage
#  flask db init   Initialize
#  flask db migrate   Generate version file
#  flask db upgrade   Synchronize to database
