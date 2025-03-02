from cracksql.config.cache import cache
from cracksql.config.db_config import db
from cracksql.config.logging_config import logger
from cracksql.models import DatabaseConfig, DatabaseType


@cache.memoize(timeout=864000, make_name="support_database_options")
def get_support_database_options():
    """Get supported database types list"""
    return DatabaseType.choices()


@cache.memoize(timeout=864000, make_name="database_config_list")
def database_config_list(limit: int, offset: int, keyword: str = None):
    """Get database configuration list"""
    try:
        query = DatabaseConfig.query
        if keyword:
            query = query.filter(DatabaseConfig.database.contains(keyword))
        total = query.count()
        configs = query.order_by(DatabaseConfig.created_at.desc()).limit(limit).offset(offset).all()

        return {
            'total': total,
            'data': [{
                'id': config.id,
                'database': config.database,
                'host': config.host,
                'port': config.port,
                'username': config.username,
                'password': config.password,
                'db_type': config.db_type,
                'description': config.description
            } for config in configs] if configs else []
        }
    except Exception as e:
        logger.error(f"database_config_list error: {e}")
        return {'total': 0, 'data': []}


@cache.memoize(timeout=864000, make_name="database_config")
def get_database_config(id: int):
    """Get single database configuration"""
    try:
        config = DatabaseConfig.query.get(id)
        return {'data': {
            'id': config.id,
            'database': config.database,
            'host': config.host,
            'port': config.port,
            'username': config.username,
            'password': config.password,
            'db_type': config.db_type,
            'description': config.description
        }} if config else None
    except Exception as e:
        logger.error(f"get_database_config error: {e}")
        return None


def insert_database_config(host: str, port: int, database: str,
                           username: str, password: str, db_type: str,
                           description: str = None) -> bool:
    """Create database configuration"""
    try:
        config = DatabaseConfig(
            host=host,
            port=port,
            database=database,
            username=username,
            password=password,
            db_type=db_type,
            description=description
        )

        db.session.add(config)
        db.session.commit()
        cache.delete_memoized(database_config_list)
        return True
    except Exception as e:
        logger.error(f"insert_database_config error: {e}")
        db.session.rollback()
        return False


def update_database_config(id: int, host: str, port: int, database: str,
                           username: str, password: str, db_type: str,
                           description: str = None) -> bool:
    """Update database configuration"""
    try:
        config = DatabaseConfig.query.get(id)
        if not config:
            logger.error(f"update_database_config error: config id {id} not found")
            return False

        config.host = host
        config.port = port
        config.database = database
        config.username = username
        config.password = password
        config.db_type = db_type
        config.description = description

        db.session.commit()
        cache.delete_memoized(database_config_list)
        cache.delete_memoized(get_database_config, id)
        return True
    except Exception as e:
        logger.error(f"update_database_config error: {e}")
        db.session.rollback()
        return False


def delete_database_config(id: int) -> bool:
    """Delete database configuration"""
    try:
        config = DatabaseConfig.query.get(id)
        if not config:
            logger.error(f"delete_database_config error: config id {id} not found")
            return False

        db.session.delete(config)
        db.session.commit()
        cache.delete_memoized(database_config_list)
        cache.delete_memoized(get_database_config, id)
        return True
    except Exception as e:
        logger.error(f"delete_database_config error: {e}")
        db.session.rollback()
        return False
