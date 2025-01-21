from api.utils.response import ResMsg
from api.utils.util import route
from flask import Blueprint, request
from api.services.llm_model import LLMModelService


bp = Blueprint("llm_model", __name__, url_prefix='/api/llm_model')


@route(bp, '/create', methods=['POST'])
def create_model():
    """创建模型"""
    res = ResMsg()
    try:
        data = request.get_json()
        model = LLMModelService.create_model(data)
        res.update(data=model)
    except ValueError as e:
        res.update(code=400, msg=str(e))
    except Exception as e:
        res.update(code=500, msg=f"创建模型失败: {str(e)}")
    return res.data


@route(bp, '/update', methods=['POST'])
def update_model():
    """更新模型"""
    res = ResMsg()
    try:
        data = request.get_json()
        model_id = data.get('id')
        if not model_id:
            res.update(code=400, msg="缺少模型ID")
            return res.data

        result = LLMModelService.update_model(model_id, data)
        if not result:
            res.update(code=404, msg="模型不存在")
            return res.data
        res.update(data=result)
    except ValueError as e:
        res.update(code=400, msg=str(e))
    except Exception as e:
        res.update(code=500, msg=f"更新模型失败: {str(e)}")
    return res.data


@route(bp, '/delete', methods=['POST'])
def delete_model():
    """删除模型"""
    res = ResMsg()
    try:
        data = request.get_json()
        model_id = data.get('id')
        if not model_id:
            res.update(code=400, msg="缺少模型ID")
            return res.data

        success = LLMModelService.delete_model(model_id)
        if not success:
            res.update(code=404, msg="模型不存在")
            return res.data
        res.update(msg="删除成功")
    except Exception as e:
        res.update(code=500, msg=f"删除模型失败: {str(e)}")
    return res.data


@route(bp, '/detail', methods=['GET'])
def get_model():
    """获取模型详情"""
    res = ResMsg()
    try:
        model_id = request.args.get('id')
        if not model_id:
            res.update(code=400, msg="缺少模型ID")
            return res.data

        model = LLMModelService.get_model(int(model_id))
        if not model:
            res.update(code=404, msg="模型不存在")
            return res.data
        res.update(data=model)
    except Exception as e:
        res.update(code=500, msg=f"获取模型失败: {str(e)}")
    return res.data


@route(bp, '/llm_models', methods=['GET'])
def get_models():
    """获取模型列表"""
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
        res.update(code=500, msg=f"获取模型列表失败: {str(e)}")
    return res.data