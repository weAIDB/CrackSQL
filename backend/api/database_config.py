from flask import Blueprint, request
from api.utils.code import ResponseCode
from api.utils.response import ResMsg
from api.utils.util import route
from api.services.database_config import (
    database_config_list, get_database_config,
    insert_database_config, update_database_config,
    delete_database_config, get_support_database_options
)

bp = Blueprint("database_config", __name__, url_prefix='/api/database_config')


@route(bp, '/support', methods=["GET"])
def support_api():
    """获取支持的数据库类型列表"""
    res = ResMsg()
    res.update(data=get_support_database_options())
    return res.data


@route(bp, '/list', methods=["POST"])
def list_api():
    """获取数据库配置列表"""
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
    """获取数据库配置详情"""
    res = ResMsg()
    obj = request.get_json(force=True)
    config_id = obj.get('id')
    
    if not config_id:
        res.update(code=ResponseCode.InvalidParameter, msg="配置ID不能为空")
        return res.data
        
    data = get_database_config(id=config_id)
    if not data:
        res.update(code=ResponseCode.Fail, msg="配置不存在")
        return res.data
        
    res.update(data=data)
    return res.data


@route(bp, '/types', methods=["GET"])
def types_api():
    """获取支持的数据库类型列表"""
    res = ResMsg()
    res.update(data={'types': DatabaseType.choices()})
    return res.data


@route(bp, '/create', methods=["POST"])
def create_api():
    """创建数据库配置"""
    res = ResMsg()
    obj = request.get_json(force=True)
    
    # 必填字段验证
    required_fields = ['host', 'port', 'database', 'username', 'password', 'db_type']
    for field in required_fields:
        if not obj.get(field):
            res.update(code=ResponseCode.InvalidParameter, msg=f"{field}不能为空")
            return res.data
    
    # 验证数据库类型是否有效
    if obj['db_type'] not in [t.value for t in DatabaseType]:
        res.update(code=ResponseCode.InvalidParameter, msg="无效的数据库类型")
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
        res.update(code=ResponseCode.Fail, msg="创建失败")
        return res.data
        
    res.update(data=result)
    return res.data


@route(bp, '/update', methods=["POST"])
def update_api():
    """更新数据库配置"""
    res = ResMsg()
    obj = request.get_json(force=True)
    
    # 验证ID
    config_id = obj.get('id')
    if not config_id:
        res.update(code=ResponseCode.InvalidParameter, msg="配置ID不能为空")
        return res.data
    
    # 必填字段验证
    required_fields = ['host', 'port', 'database', 'username', 'password', 'db_type']
    for field in required_fields:
        if not obj.get(field):
            res.update(code=ResponseCode.InvalidParameter, msg=f"{field}不能为空")
            return res.data
    
    # 验证数据库类型是否有效
    if obj['db_type'] not in [t.value for t in DatabaseType]:
        res.update(code=ResponseCode.InvalidParameter, msg="无效的数据库类型")
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
    """删除数据库配置"""
    res = ResMsg()
    obj = request.get_json(force=True)
    config_id = obj.get('id')
    
    if not config_id:
        res.update(code=ResponseCode.InvalidParameter, msg="配置ID不能为空")
        return res.data
        
    result = delete_database_config(id=config_id)
    if not result:
        res.update(code=ResponseCode.Fail, msg="删除失败")
        return res.data
        
    res.update(data=result)
    return res.data 