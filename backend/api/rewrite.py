from flask import Blueprint, request
from api.utils.code import ResponseCode
from api.utils.response import ResMsg
from api.utils.util import route
from api.services.rewrite import RewriteService
import asyncio

bp = Blueprint('rewrite', __name__, url_prefix='/api/rewrite')


@route(bp, '/list', methods=['POST'])
def list_api():
    """获取改写列表"""
    res = ResMsg()
    obj = request.get_json(force=True)
    limit = obj.get('page_size', 20)
    offset = limit * obj.get('page', 0)
    keyword = obj.get('keyword', None)
    
    try:
        result = RewriteService.get_history_list(offset + 1, limit, keyword)
        res.update(data={
            'total': result['total'],
            'data': result['data']
        })
    except Exception as e:
        res.update(code=ResponseCode.Fail, msg=str(e))
    
    return res.data


@route(bp, '/detail', methods=['POST'])
def detail_api():
    """获取改写详情"""
    res = ResMsg()
    obj = request.get_json(force=True)
    history_id = obj.get('id')
    
    if not history_id:
        res.update(code=ResponseCode.InvalidParameter, msg="历史记录ID不能为空")
        return res.data
    
    try:
        result = RewriteService.get_history_by_id(history_id)
        if not result:
            res.update(code=ResponseCode.NotFound, msg="历史记录不存在")
            return res.data
            
        res.update(data=result)
    except Exception as e:
        res.update(code=ResponseCode.Fail, msg=str(e))
    
    return res.data


@route(bp, '/latest', methods=['GET'])
def latest_api():
    """获取最近一次改写记录"""
    res = ResMsg()
    
    try:
        result = RewriteService.get_latest_history()
        if not result:
            res.update(code=ResponseCode.Success, msg="暂无历史记录")
            return res.data
            
        res.update(data=result)
    except Exception as e:
        res.update(code=ResponseCode.Fail, msg=str(e))
    
    return res.data


@route(bp, '/create', methods=['POST'])
def create_api():
    """创建改写历史"""
    res = ResMsg()
    obj = request.get_json(force=True)
    
    try:
        result = RewriteService.create_history(
            source_db_type=obj['source_db_type'],
            original_sql=obj['original_sql'],
            target_db_type=obj['target_db_type'],
            target_db_user=obj['target_db_user'],
            target_db_host=obj['target_db_host'],
            target_db_port=obj['target_db_port'],
            target_db_password=obj['target_db_password'],
            target_db_database=obj['target_db_database'],
            target_db_id=obj['target_db_id']
        )
        
        # 异步启动改写任务
        history_id = result['id']
        asyncio.create_task(RewriteService.process_rewrite_task(history_id))
        
        res.update(data=result)
    except Exception as e:
        res.update(code=ResponseCode.Fail, msg=str(e))
    
    return res.data
