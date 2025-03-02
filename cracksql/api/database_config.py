from flask import Blueprint, request

from cracksql.models import DatabaseType
from cracksql.api.utils.code import ResponseCode
from cracksql.api.utils.response import ResMsg
from cracksql.api.utils.util import route
from cracksql.api.services.database_config import (
    database_config_list, get_database_config,
    insert_database_config, update_database_config,
    delete_database_config, get_support_database_options
)

bp = Blueprint("database_config", __name__, url_prefix='/api/database_config')


@route(bp, '/support', methods=["GET"])
def support_api():
    """Get supported database types list"""
    res = ResMsg()
    res.update(data=get_support_database_options())
    return res.data


@route(bp, '/list', methods=["POST"])
def list_api():
    """Get database configuration list"""
    res = ResMsg()
    obj = request.get_json(force=True)
    limit = obj.get('page_size', 10)
    offset = limit * obj.get("page", 0)
    keyword = obj.get('keyword', None)
    data = database_config_list(limit=limit, offset=offset, keyword=keyword)
    res.update(data=data)
    return res.data


@route(bp, '/detail', methods=["POST"])
def detail_api():
    """Get database configuration details"""
    res = ResMsg()
    obj = request.get_json(force=True)
    config_id = obj.get('id')

    if not config_id:
        res.update(code=ResponseCode.InvalidParameter, msg="Configuration ID cannot be empty")
        return res.data

    data = get_database_config(id=config_id)
    if not data:
        res.update(code=ResponseCode.Fail, msg="Configuration does not exist")
        return res.data

    res.update(data=data)
    return res.data


@route(bp, '/types', methods=["GET"])
def types_api():
    """Get supported database types list"""
    res = ResMsg()
    res.update(data={'types': DatabaseType.choices()})
    return res.data


@route(bp, '/create', methods=["POST"])
def create_api():
    """Create database configuration"""
    res = ResMsg()
    obj = request.get_json(force=True)

    # Verify required fields
    required_fields = ['host', 'port', 'database', 'username', 'password', 'db_type']
    for field in required_fields:
        if not obj.get(field):
            res.update(code=ResponseCode.InvalidParameter, msg=f"{field} cannot be empty")
            return res.data

    # Verify if the database type is valid
    if obj['db_type'] not in [t.value for t in DatabaseType]:
        res.update(code=ResponseCode.InvalidParameter, msg="Invalid database type")
        return res.data

    result = insert_database_config(
        host=obj['host'],
        port=int(obj['port']),
        database=obj['database'],
        username=obj['username'],
        password=obj['password'],
        db_type=obj['db_type'],
        description=obj.get('description')
    )

    if not result:
        res.update(code=ResponseCode.Fail, msg="Create failed")
        return res.data

    res.update(data=result)
    return res.data


@route(bp, '/update', methods=["POST"])
def update_api():
    """Update database configuration"""
    res = ResMsg()
    obj = request.get_json(force=True)

    # Verify ID
    config_id = obj.get('id')
    if not config_id:
        res.update(code=ResponseCode.InvalidParameter, msg="Configuration ID cannot be empty")
        return res.data

    # Verify required fields
    required_fields = ['host', 'port', 'database', 'username', 'password', 'db_type']
    for field in required_fields:
        if not obj.get(field):
            res.update(code=ResponseCode.InvalidParameter, msg=f"{field} cannot be empty")
            return res.data

    # Verify if the database type is valid
    if obj['db_type'] not in [t.value for t in DatabaseType]:
        res.update(code=ResponseCode.InvalidParameter, msg="Invalid database type")
        return res.data

    result = update_database_config(
        id=config_id,
        host=obj['host'],
        port=int(obj['port']),
        database=obj['database'],
        username=obj['username'],
        password=obj['password'],
        db_type=obj['db_type'],
        description=obj.get('description')
    )

    if not result:
        res.update(code=ResponseCode.Fail, msg="更新失败")
        return res.data

    res.update(data=result)
    return res.data


@route(bp, '/delete', methods=["POST"])
def delete_api():
    """Delete database configuration"""
    res = ResMsg()
    obj = request.get_json(force=True)
    config_id = obj.get('id')

    if not config_id:
        res.update(code=ResponseCode.InvalidParameter, msg="Configuration ID cannot be empty")
        return res.data

    result = delete_database_config(id=config_id)
    if not result:
        res.update(code=ResponseCode.Fail, msg="Delete failed")
        return res.data

    res.update(data=result)
    return res.data
