from config.db_config import db
from models import DatabaseConfig
from config.cache import cache
from api.utils.model_to_dict import query_to_dict
from config.logging_config import logger


@cache.memoize(timeout=864000, make_name="database_config_list")
def database_config_list(limit: int, offset: int, keyword: str = None):
    """获取数据库配置列表"""
    try:
        query = DatabaseConfig.query
        if keyword:
            query = query.filter(DatabaseConfig.database.contains(keyword))
        total = query.count()
        configs = query.order_by(DatabaseConfig.created_at.desc()).limit(limit).offset(offset).all()

        return {
            'total': total,
            'data': query_to_dict(configs) if configs else []
        }
    except Exception as e:
        logger.error(f"database_config_list error: {e}")
        return {'total': 0, 'data': []}


@cache.memoize(timeout=864000, make_name="database_config")
def get_database_config(id: int):
    """获取单个数据库配置"""
    try:
        config = DatabaseConfig.query.get(id)
        return {'data': query_to_dict(config)} if config else None
    except Exception as e:
        logger.error(f"get_database_config error: {e}")
        return None


def insert_database_config(host: str, port: int, database: str, 
                         username: str, password: str, db_type: str,
                         description: str = None) -> bool:
    """创建数据库配置"""
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
    """更新数据库配置"""
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
    """删除数据库配置"""
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