from flask import Blueprint, request
from api.utils.code import ResponseCode
from api.utils.response import ResMsg
from api.utils.util import route
from api.services.rewrite import RewriteService
from api.utils.scheduler import scheduler

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
        result = RewriteService.get_history_list(offset, limit, keyword)
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
            res.update(code=ResponseCode.NoResourceFound, msg="历史记录不存在")
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
            source_kb_id=obj['source_kb_id'],
            target_kb_id=obj['target_kb_id'],
            target_db_id=obj['target_db_id'],
            llm_model_name=obj['llm_model_name']
        )
        
        # 使用scheduler添加任务，移除asyncio.create_task调用
        scheduler.add_job(
            func=RewriteService.process_rewrite_task,
            args=[result['id']],
            id=f'rewrite_task_{result["id"]}',
            trigger='date',
            misfire_grace_time=None,
            max_instances=1
        )
        
        res.update(data=result)
    except Exception as e:
        res.update(code=ResponseCode.Fail, msg=str(e))
    
    return res.data
