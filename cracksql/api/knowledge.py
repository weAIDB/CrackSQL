import datetime
from flask import Blueprint, request, jsonify, session

from cracksql.task.task import process_json_data
from cracksql.api.utils.code import ResponseCode
from cracksql.api.utils.response import ResMsg
from cracksql.api.utils.scheduler import scheduler
from cracksql.api.utils.util import route
from cracksql.api.services.knowledge import (
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

bp = Blueprint("knowledge", __name__, url_prefix='/api/knowledge_base')


@route(bp, '/list', methods=["GET"])
def list_knowledge_bases():
    """Get knowledge base list"""
    res = ResMsg()
    try:
        data = get_knowledge_base_list()
        res.update(data=data)
        return res.data
    except Exception as e:
        res.update(code=ResponseCode.Fail, msg=str(e))
        return res.data


@route(bp, '/detail', methods=["GET"])
def get_kb():
    """Get single knowledge base information"""
    res = ResMsg()
    kb_name = request.args.get('kb_name')

    if not kb_name:
        res.update(code=ResponseCode.InvalidParameter, msg="Knowledge base name cannot be empty")
        return res.data

    try:
        data = get_knowledge_base(kb_name)
        if not data:
            res.update(code=ResponseCode.NoResourceFound, msg="Knowledge base does not exist")
            return res.data

        res.update(data=data)
        return res.data
    except Exception as e:
        res.update(code=ResponseCode.Fail, msg=str(e))
        return res.data


@route(bp, '/create', methods=["POST"])
def create_kb():
    """Create knowledge base"""
    res = ResMsg()
    data = request.get_json(force=True)

    # Verify required parameters
    required_fields = ['kb_name', 'embedding_model_name']
    for field in required_fields:
        if not data.get(field):
            res.update(code=ResponseCode.InvalidParameter, msg=f"Missing required parameter: {field}")
            return res.data

    try:
        # Create knowledge base
        result = create_knowledge_base(
            kb_name=data.get('kb_name'),
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
def update_kb():
    """Update knowledge base"""
    res = ResMsg()
    data = request.get_json(force=True)
    kb_id = data.get('kb_id')

    if not kb_id:
        res.update(code=ResponseCode.InvalidParameter, msg="Knowledge base ID cannot be empty")
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
def delete_kb():
    """Delete knowledge base"""
    res = ResMsg()
    data = request.get_json(force=True)
    kb_name = data.get('kb_name')

    if not kb_name:
        res.update(code=ResponseCode.InvalidParameter, msg="Knowledge base name cannot be empty")
        return res.data

    try:
        # Get knowledge base information
        kb = get_knowledge_base(kb_name)
        if not kb:
            res.update(code=ResponseCode.NoResourceFound, msg="Knowledge base does not exist")
            return res.data

        # Delete knowledge base and associated data
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
def search_kb():
    """Search knowledge base"""
    res = ResMsg()
    data = request.get_json(force=True)

    if not all([data.get('kb_name'), data.get('query')]):
        res.update(code=ResponseCode.InvalidParameter, msg="Knowledge base name and search query cannot be empty")
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
def upload_json():
    """Upload JSON file"""
    res = ResMsg()
    try:
        file = request.files.get('file')
        kb_name = request.form.get('kb_name')

        if not file or not kb_name:
            res.update(code=ResponseCode.InvalidParameter, msg="Missing required parameters")
            return res.data

        if not file.filename.endswith('.json'):
            res.update(code=ResponseCode.InvalidParameter, msg="Only JSON files are supported")
            return res.data

        result = upload_json_file(kb_name, file)
        res.update(data=result)
        return res.data

    except Exception as e:
        res.update(code=ResponseCode.Fail, msg=str(e))
        return res.data


@route(bp, '/items', methods=['GET'])
def get_items():
    """Get JSON records"""
    res = ResMsg()
    try:
        kb_name = request.args.get('kb_name')
        if not kb_name:
            res.update(code=ResponseCode.InvalidParameter, msg="Knowledge base name cannot be empty")
            return res.data

        # Get pagination
        page = request.args.get('page', 1)
        page_size = request.args.get('page_size', 10)

        items = get_json_items(kb_name, page, page_size)
        res.update(data=items)
        return res.data
    except Exception as e:
        res.update(code=ResponseCode.Fail, msg=str(e))
        return res.data


@route(bp, '/add_items', methods=['POST'])
def add_items():
    """Add JSON records (supports single or batch)"""
    res = ResMsg()
    try:
        data = request.get_json()
        kb_name = data.get('kb_name')
        items = data.get('items')  # Can be a single object or an object array

        if not kb_name or not items:
            res.update(code=ResponseCode.InvalidParameter, msg="Missing required parameters or format error")
            return res.data

        # If the input is a single object, convert it to a list
        if not isinstance(items, list):
            items = [items]

        # Call the add method
        result = add_kb_items(kb_name, items)
        res.update(data=result)
        return res.data

    except Exception as e:
        res.update(code=ResponseCode.Fail, msg=str(e))
        return res.data


@route(bp, '/delete_items', methods=['POST'])
def delete_items():
    """Delete knowledge base items"""
    res = ResMsg()
    try:
        data = request.get_json()
        kb_name = data.get('kb_name')
        item_ids = data.get('item_ids')  # Optional parameter

        if not kb_name:
            res.update(code=ResponseCode.InvalidParameter, msg="Missing knowledge base name")
            return res.data

        # Verify item_ids format
        if item_ids is not None:
            if not isinstance(item_ids, list) or not all(isinstance(id, int) for id in item_ids):
                res.update(code=ResponseCode.InvalidParameter, msg="item_ids must be an integer ID list")
                return res.data

        result = delete_kb_items(kb_name, item_ids)
        res.update(data=result)
        return res.data

    except Exception as e:
        res.update(code=ResponseCode.Fail, msg=str(e))
        return res.data


@route(bp, '/vectorize_items', methods=['POST'])
def vectorize_items():
    """Vectorize knowledge base items"""
    res = ResMsg()
    try:
        data = request.get_json()
        kb_name = data.get('kb_name')
        item_ids = data.get('item_ids')  # Optional parameter

        if not kb_name:
            res.update(code=ResponseCode.InvalidParameter, msg="Missing knowledge base name")
            return res.data

        # Verify item_ids format (if provided)
        if item_ids is not None:
            if not isinstance(item_ids, list) or not all(isinstance(id, int) for id in item_ids):
                res.update(code=ResponseCode.InvalidParameter, msg="item_ids must be an integer ID list")
                return res.data

        # Call the vectorization task
        job_id = f"vectorize_items_{kb_name}"
        scheduler.add_job(
            func=process_json_data,
            args=[kb_name, item_ids],
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
