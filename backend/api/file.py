import os

from flask import Blueprint, request, send_from_directory, current_app
import mimetypes
from api.utils.auth import login_required
from api.utils.code import ResponseCode
from api.utils.response import ResMsg
from api.utils.util import route
from api.services.file import process_uploaded_file


bp = Blueprint("file", __name__, url_prefix='/api/file')


@route(bp, '/test', methods=["GET"])
def test():
    """
    测试接口
    :return:
    """
    res = ResMsg()
    data = {'status': True}
    res.update(data=data)
    return res.data


@route(bp, '/upload_file', methods=["POST"])
@login_required
def upload_file():
    """
    文件上传接口
    :return:
    """
    res = ResMsg()
    file = request.files.get('file', None)
    print("===已经接收到文件")
    if not file:
        res.update(code=ResponseCode.InvalidParameter)
        return res.data

    print("===保存文件")
    result = process_uploaded_file(file)
    print("===保存文件成功")
    res.update(data=result)
    return res.data

