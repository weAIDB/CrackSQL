import base64
import io
import random
import re
import string
from functools import wraps

from PIL import Image, ImageFont, ImageDraw
from flask import jsonify, Response
from api.utils.response import ResMsg
from config import cache


def route(bp, *args, **kwargs):
    """
    路由设置,统一返回格式
    :param bp: 蓝图
    :param args:
    :param kwargs:
    :return:
    """
    kwargs.setdefault('strict_slashes', False)

    def decorator(f):
        @bp.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*args, **kwargs):
            rv = f(*args, **kwargs)
            # 响应函数返回整数和浮点型
            if isinstance(rv, (int, float)):
                res = ResMsg()
                res.update(data=rv)
                return jsonify(res.data)
            # 响应函数返回元组
            elif isinstance(rv, tuple):
                # 判断是否为多个参数，且第一个参数不是Response对象
                if len(rv) >= 3 and not isinstance(rv[0], Response):
                    return jsonify(rv[0]), rv[1], rv[2]
                elif not isinstance(rv[0], Response):
                    return jsonify(rv[0]), rv[1]
                else:
                    return rv  # 直接返回Response对象
            # 响应函数返回字典
            elif isinstance(rv, dict):
                return jsonify(rv)
            # 响应函数返回字节
            elif isinstance(rv, bytes):
                rv = rv.decode('utf-8')
                return jsonify(rv)
            # 如果响应函数返回的是Flask Response对象或其他非字符串/bytes类型
            elif isinstance(rv, Response):
                return rv
            # 其他情况：尝试直接返回，可能是文件等情况
            else:
                return rv

        return wrapper

    return decorator


def view_route(f):
    """
    路由设置,统一返回格式
    :param f:
    :return:
    """

    def decorator(*args, **kwargs):
        rv = f(*args, **kwargs)
        if isinstance(rv, (int, float)):
            res = ResMsg()
            res.update(data=rv)
            return jsonify(res.data)
        elif isinstance(rv, tuple):
            if len(rv) >= 3:
                return jsonify(rv[0]), rv[1], rv[2]
            else:
                return jsonify(rv[0]), rv[1]
        elif isinstance(rv, dict):
            return jsonify(rv)
        elif isinstance(rv, bytes):
            rv = rv.decode('utf-8')
            return jsonify(rv)
        else:
            return jsonify(rv)

    return decorator
