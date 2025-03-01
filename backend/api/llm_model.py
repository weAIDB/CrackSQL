import logging

from api.utils.response import ResMsg
from api.utils.util import route
from flask import Blueprint, request
from api.services.llm_model import LLMModelService


bp = Blueprint("llm_model", __name__, url_prefix='/api/llm_model')


@route(bp, '/create', methods=['POST'])
def create_model():
    """Create model"""
    res = ResMsg()
    try:
        data = request.get_json()
        model = LLMModelService.create_model(data)
        res.update(data=model)
    except ValueError as e:
        res.update(code=400, msg=str(e))
    except Exception as e:
        res.update(code=500, msg=f"Create model failed: {str(e)}")
    return res.data


@route(bp, '/update', methods=['POST'])
def update_model():
    """Update model"""
    res = ResMsg()
    try:
        data = request.get_json()
        model_id = data.get('id')
        if not model_id:
            res.update(code=400, msg="Missing model ID")
            return res.data

        result = LLMModelService.update_model(model_id, data)
        if not result:
            res.update(code=404, msg="Model does not exist")
            return res.data
        res.update(data=result)
    except ValueError as e:
        res.update(code=400, msg=str(e))
    except Exception as e:
        res.update(code=500, msg=f"Update model failed: {str(e)}")
    return res.data


@route(bp, '/delete', methods=['POST'])
def delete_model():
    """Delete model"""
    res = ResMsg()
    try:
        data = request.get_json()
        model_id = data.get('id')
        if not model_id:
            res.update(code=400, msg="Missing model ID")
            return res.data

        success = LLMModelService.delete_model(model_id)
        if not success:
            res.update(code=404, msg="Model does not exist")
            return res.data
        res.update(msg="Delete successfully")
    except Exception as e:
        res.update(code=500, msg=f"删除模型失败: {str(e)}")
    return res.data


@route(bp, '/detail', methods=['GET'])
def get_model():
    """Get model detail"""
    res = ResMsg()
    try:
        model_id = request.args.get('id')
        if not model_id:
            res.update(code=400, msg="Missing model ID")
            return res.data

        model = LLMModelService.get_model(int(model_id))
        if not model:
            res.update(code=404, msg="Model does not exist")
            return res.data
        res.update(data=model)
    except Exception as e:
        res.update(code=500, msg=f"Get model failed: {str(e)}")
    return res.data


@route(bp, '/llm_models', methods=['GET'])
def get_models():
    """Get model list"""
    res = ResMsg()
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        search = request.args.get('search')
        deployment_type = request.args.get('deployment_type')
        category = request.args.get('category')
        is_active = request.args.get('is_active')
        if is_active is not None:
            is_active = is_active.lower() == 'true'

        models, total = LLMModelService.get_models(
            page=page,
            per_page=per_page,
            search=search,
            deployment_type=deployment_type,
            category=category,
            is_active=is_active
        )

        res.update(data={
            'items': models,
            'total': total,
            'page': page,
            'per_page': per_page
        })
    except ValueError as e:
        res.update(code=400, msg=str(e))
    except Exception as e:
        res.update(code=500, msg=f"Get model list failed: {str(e)}")
    return res.data


@route(bp, '/release_all_llm_models', methods=['POST'])
def release_all_llm_models():
    """Release all models"""
    res = ResMsg()
    LLMModelService.release_all_llm_models()
    res.update(msg="Release successfully")
    return res.data


@route(bp, '/release_llm_model', methods=['POST'])
def release_llm_model():
    """Release model"""
    res = ResMsg()
    data = request.get_json()
    if not data.get('model_name'):
        res.update(code=400, msg="Missing model name")
        return res.data
    LLMModelService.release_llm_model(data.get('model_name'))
    res.update(msg="Release successfully")
    return res.data


@route(bp, '/load_llm_model', methods=['POST'])
def load_llm_model():
    """Load model"""
    res = ResMsg()
    data = request.get_json()
    logging.info("load_model", data.get('model_name'))
    if not data.get('model_name'):
        res.update(code=400, msg="Missing model name")
        return res.data
    LLMModelService.load_llm_model(data.get('model_name'))
    res.update(msg="Load successfully")
    return res.data


@route(bp, '/load_embedding', methods=['POST'])
def load_embedding():
    """Load Embedding model"""
    res = ResMsg()
    data = request.get_json()
    if not data.get('model_name'):
        res.update(code=400, msg="Missing model name")
        return res.data
    LLMModelService.load_embedding(data.get('model_name'))
    res.update(msg="Load successfully")
    return res.data


@route(bp, '/release_all_embeddings', methods=['POST'])
def release_all_embeddings():
    """Release all Embedding models"""
    res = ResMsg()
    LLMModelService.release_all_embeddings()
    res.update(msg="Release successfully")
    return res.data


@route(bp, '/release_embedding', methods=['POST'])
def release_embedding():
    """Release Embedding model"""
    res = ResMsg()
    data = request.get_json()
    if not data.get('model_name'):
        res.update(code=400, msg="Missing model name")
        return res.data
    LLMModelService.release_embedding(data.get('model_name'))
    res.update(msg="Release successfully")
    return res.data
