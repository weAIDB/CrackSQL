import logging
from flask import Blueprint, request
from api.utils.code import ResponseCode
from api.utils.response import ResMsg
from api.utils.util import route
from api.utils.auth import Auth, login_required
from api.services.password_login_or_register import password_login, password_update, password_register

bp = Blueprint("user", __name__, url_prefix='/api/user')

logger = logging.getLogger(__name__)


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


@route(bp, '/login', methods=["POST"])
def login():
    """
    登陆成功获取到数据获取token和刷新token
    :return:
    """
    res = ResMsg()
    obj = request.get_json(force=True)
    user_name = obj.get("username")
    password = obj.get("password")
    # 未获取到参数或参数不存在
    if not obj or not user_name or not password:
        res.update(code=ResponseCode.InvalidParameter)
        return res.data

    user = password_login(user_name=user_name, password=password)

    if not user:
        res.update(code=ResponseCode.AccountOrPassWordErr)
        return res.data

    # 生成数据获取token和刷新token
    access_token, refresh_token = Auth.encode_auth_token(
        user_id=user['id'], exp=720)
    user["access_token"] = access_token
    user["refresh_token"] = refresh_token
    res.update(data=user)
    return res.data


@route(bp, '/password/update', methods=["POST"])
# @login_required
def update_password():
    """
    更新密码
    :return:
    """
    res = ResMsg()
    obj = request.get_json(force=True)
    old_password = obj.get("old_password")
    new_password = obj.get("new_password")
    user_id = obj.get("user_id")
    if (not old_password) or (not new_password) or (not user_id):
        res.update(code=ResponseCode.InvalidParameter)
        return res.data

    result = password_update(
        user_id=user_id,
        old_password=old_password,
        new_password=new_password)

    if not result:
        res.update(code=ResponseCode.AccountOrPassWordErr, msg="密码错误")
        return res.data

    res.update(data=result)
    return res.data


@route(bp, '/refreshToken', methods=["GET"])
# @login_required
def refresh_token():
    """
    刷新token，获取新的数据获取token
    :return:
    """
    res = ResMsg()
    refresh_token = request.args.get("refresh_token")
    if not refresh_token:
        res.update(code=ResponseCode.InvalidParameter)
        return res.data
    payload = Auth.decode_auth_token(refresh_token)
    # token被串改或过期
    if not payload:
        res.update(code=ResponseCode.PleaseSignIn)
        return res.data

    # 判断token正确性
    if "user_id" not in payload:
        res.update(code=ResponseCode.PleaseSignIn)
        return res.data
    # 获取新的token
    access_token = Auth.generate_access_token(user_id=payload["user_id"])
    data = {"access_token": access_token.decode(
        "utf-8"), "refresh_token": refresh_token}
    res.update(data=data)
    return res.data


@route(bp, '/register', methods=["POST"])
def register():
    """
    注册
    :return:
    """
    res = ResMsg()
    obj = request.get_json(force=True)
    name = obj.get("username", None)
    passwd = obj.get("password", None)

    # 参数错误
    if name is None or passwd is None:
        res.update(code=ResponseCode.InvalidParameter)
        return res.data

    data = password_register(name, passwd, obj.get("level"))
    if data is None:
        res.update(code=ResponseCode.Fail)
        return res.data
    res.update(data=data)
    return res.data
