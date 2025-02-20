import datetime

from flask import Blueprint, request, jsonify, session
from api.utils.code import ResponseCode
from api.utils.response import ResMsg
from api.utils.scheduler import scheduler
from api.utils.util import route
from api.utils.auth import login_required
from api.services.knowledge import (
    create_knowledge_base,
    get_knowledge_base_list,
    get_knowledge_base,
    update_knowledge_base,
    delete_knowledge_base,
    search_knowledge_base,
    upload_json_file,
    delete_kb_items,
    get_json_items,
    add_kb_items
)
from task.task import process_json_data

bp = Blueprint("knowledge", __name__, url_prefix='/api/knowledge_base')


@route(bp, '/list', methods=["GET"])
# @login_required
def list_knowledge_bases():
    """获取知识库列表"""
    res = ResMsg()
    try:
        data = get_knowledge_base_list()
        res.update(data=data)
        return res.data
    except Exception as e:
        res.update(code=ResponseCode.Fail, msg=str(e))
        return res.data


@route(bp, '/detail', methods=["GET"])
# @login_required
def get_kb():
    """获取单个知识库信息"""
    res = ResMsg()
    kb_name = request.args.get('kb_name')

    if not kb_name:
        res.update(code=ResponseCode.InvalidParameter, msg="知识库名称不能为空")
        return res.data

    try:
        data = get_knowledge_base(kb_name)
        if not data:
            res.update(code=ResponseCode.NoResourceFound, msg="知识库不存在")
            return res.data

        res.update(data=data)
        return res.data
    except Exception as e:
        res.update(code=ResponseCode.Fail, msg=str(e))
        return res.data


@route(bp, '/create', methods=["POST"])
# @login_required
def create_kb():
    """创建知识库"""
    res = ResMsg()
    data = request.get_json(force=True)
    user_id = session.get('user_id')

    # 验证必要参数
    required_fields = ['kb_name', 'embedding_model_name']
    for field in required_fields:
        if not data.get(field):
            res.update(code=ResponseCode.InvalidParameter, msg=f"缺少必要参数: {field}")
            return res.data

    try:
        # 创建知识库
        result = create_knowledge_base(
            kb_name=data.get('kb_name'),
            user_id=user_id,
            kb_info=data.get('kb_info'),
            embedding_model_name=data.get('embedding_model_name'),
            db_type=data.get('db_type')
        )

        if not result['status']:
            res.update(code=ResponseCode.Fail, msg=result['msg'])
            return res.data

        res.update(data=result.get('data'))
        return res.data
    except Exception as e:
        res.update(code=ResponseCode.Fail, msg=str(e))
        return res.data


@route(bp, '/update', methods=["POST"])
# @login_required
def update_kb():
    """更新知识库"""
    res = ResMsg()
    data = request.get_json(force=True)
    kb_id = data.get('kb_id')

    if not kb_id:
        res.update(code=ResponseCode.InvalidParameter, msg="知识库ID不能为空")
        return res.data

    try:
        result = update_knowledge_base(kb_id, data)
        if not result['status']:
            res.update(code=ResponseCode.Fail, msg=result['msg'])
            return res.data

        res.update(data=result.get('data'))
        return res.data
    except Exception as e:
        res.update(code=ResponseCode.Fail, msg=str(e))
        return res.data


@route(bp, '/delete', methods=["POST"])
# @login_required
def delete_kb():
    """删除知识库"""
    res = ResMsg()
    data = request.get_json(force=True)
    kb_name = data.get('kb_name')

    if not kb_name:
        res.update(code=ResponseCode.InvalidParameter, msg="知识库名称不能为空")
        return res.data

    try:
        # 获取知识库信息
        kb = get_knowledge_base(kb_name)
        if not kb:
            res.update(code=ResponseCode.NoResourceFound, msg="知识库不存在")
            return res.data

        # 删除知识库及其关联数据
        result = delete_knowledge_base(kb_name)
        if not result['status']:
            res.update(code=ResponseCode.Fail, msg=result['msg'])
            return res.data

        res.update(data=result.get('data'))
        return res.data
    except Exception as e:
        res.update(code=ResponseCode.Fail, msg=str(e))
        return res.data


@route(bp, '/search', methods=["POST"])
# @login_required
def search_kb():
    """搜索知识库"""
    res = ResMsg()
    data = request.get_json(force=True)

    if not all([data.get('kb_name'), data.get('query')]):
        res.update(code=ResponseCode.InvalidParameter, msg="知识库名称和搜索词不能为空")
        return res.data

    try:
        results = search_knowledge_base(
            kb_name=data.get('kb_name'),
            query=data.get('query'),
            top_k=data.get('top_k', 5)
        )
        res.update(data=results)
        return res.data
    except Exception as e:
        res.update(code=ResponseCode.Fail, msg=str(e))
        return res.data


@route(bp, '/upload', methods=['POST'])
# @login_required
def upload_json():
    """上传JSON文件"""
    res = ResMsg()
    try:
        file = request.files.get('file')
        kb_name = request.form.get('kb_name')
        user_id = session.get('user_id')

        if not file or not kb_name:
            res.update(code=ResponseCode.InvalidParameter, msg="缺少必要参数")
            return res.data

        if not file.filename.endswith('.json'):
            res.update(code=ResponseCode.InvalidParameter, msg="仅支持JSON文件")
            return res.data

        result = upload_json_file(kb_name, file, user_id)
        res.update(data=result)
        return res.data

    except Exception as e:
        res.update(code=ResponseCode.Fail, msg=str(e))
        return res.data


@route(bp, '/items', methods=['GET'])
# @login_required
def get_items():
    """获取JSON记录"""
    res = ResMsg()
    try:
        kb_name = request.args.get('kb_name')
        if not kb_name:
            res.update(code=ResponseCode.InvalidParameter, msg="知识库名称不能为空")
            return res.data

        # 获取分页
        page = request.args.get('page', 1)
        page_size = request.args.get('page_size', 10)

        items = get_json_items(kb_name, page, page_size)
        res.update(data=items)
        return res.data
    except Exception as e:
        res.update(code=ResponseCode.Fail, msg=str(e))
        return res.data


@route(bp, '/add_items', methods=['POST'])
# @login_required
def add_items():
    """添加JSON记录(支持单条或批量)"""
    res = ResMsg()
    try:
        data = request.get_json()
        kb_name = data.get('kb_name')
        items = data.get('items')  # 可以是单个对象或对象数组
        user_id = session.get('user_id')

        if not kb_name or not items:
            res.update(code=ResponseCode.InvalidParameter, msg="缺少必要参数或格式错误")
            return res.data

        # 如果传入的是单个对象,转换为列表
        if not isinstance(items, list):
            items = [items]

        # 调用添加方法
        result = add_kb_items(kb_name, items, user_id)
        res.update(data=result)
        return res.data

    except Exception as e:
        res.update(code=ResponseCode.Fail, msg=str(e))
        return res.data


@route(bp, '/delete_items', methods=['POST'])
# @login_required
def delete_items():
    """删除知识库条目"""
    res = ResMsg()
    try:
        data = request.get_json()
        kb_name = data.get('kb_name')
        item_ids = data.get('item_ids')  # 可选参数

        if not kb_name:
            res.update(code=ResponseCode.InvalidParameter, msg="缺少知识库名称")
            return res.data

        # 验证item_ids格式
        if item_ids is not None:
            if not isinstance(item_ids, list) or not all(isinstance(id, int) for id in item_ids):
                res.update(code=ResponseCode.InvalidParameter, msg="item_ids必须是整数ID列表")
                return res.data

        result = delete_kb_items(kb_name, item_ids)
        res.update(data=result)
        return res.data

    except Exception as e:
        res.update(code=ResponseCode.Fail, msg=str(e))
        return res.data


@route(bp, '/vectorize_items', methods=['POST'])
# @login_required
def vectorize_items():
    """向量化知识库条目"""
    res = ResMsg()
    try:
        data = request.get_json()
        kb_name = data.get('kb_name')
        item_ids = data.get('item_ids')  # 可选参数
        user_id = session.get('user_id')

        if not kb_name:
            res.update(code=ResponseCode.InvalidParameter, msg="缺少知识库名称")
            return res.data

        # 验证item_ids格式(如果提供)
        if item_ids is not None:
            if not isinstance(item_ids, list) or not all(isinstance(id, int) for id in item_ids):
                res.update(code=ResponseCode.InvalidParameter, msg="item_ids必须是整数ID列表")
                return res.data

        # 调用向量化任务
        job_id = f"vectorize_items_{kb_name}"
        scheduler.add_job(
            func=process_json_data,
            args=[kb_name, item_ids, user_id],  # 添加user_id参数
            trigger='date',
            run_date=datetime.datetime.now(),
            id=job_id,
            replace_existing=True,
            misfire_grace_time=3600,
            coalesce=True
        )

        res.update(data={
            "status": True,
            "job_id": job_id
        })
        return res.data

    except Exception as e:
        res.update(code=ResponseCode.Fail, msg=str(e))
        return res.data
