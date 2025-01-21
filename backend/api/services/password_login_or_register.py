from config.db_config import db
from models import UserLoginMethod, User
from api.utils.model_to_dict import query_to_dict
from config.logging_config import logger


def password_login(user_name, password):
    """
    密码登录
    :param user_name: 用户名
    :param password: 密码
    :return:
    """
    # 判断用户是否存在与本系统
    user_login = UserLoginMethod.query.filter(
        UserLoginMethod.login_method == "user_name",
        UserLoginMethod.identification == user_name,
        UserLoginMethod.access_code == password).first()

    # 存在则直接返回用户信息
    if user_login:
        user = User.query.filter(
            User.id == user_login.user_id).first()
        data = query_to_dict(user)
        return data
    # 不存在则返回用户错误
    else:
        return None


def password_update(user_id, old_password, new_password):
    """
    密码更新
    :param user_id: 用户ID
    :param old_password: 旧密码
    :param new_password: 新密码
    :return:
    """
    user_login = UserLoginMethod.query.filter(
        UserLoginMethod.login_method == "user_name",
        UserLoginMethod.user_id == user_id).first()

    if user_login.access_code != old_password:
        return False

    user_login.access_code = new_password
    db.session.commit()

    return True


def password_register(user_name, passwd, level=1):
    """
    注册
    :param user_name: 用户名
    :param passwd: 密码
    :param level: 等级
    :return:
    """
    # 判断用户是否存在与本系统
    user = UserLoginMethod.query.filter(
        UserLoginMethod.login_method == "user_name",
        UserLoginMethod.identification == user_name).first()

    # 存在用户信息, 不能注册
    if user:
        logger.error(f"password_register 发现用户: {user_name}")
        return None
    # 不存在则先新建用户然后返回用户信息
    else:
        try:
            # 新建用户信息
            new_user = User(name=user_name, level=level)
            db.session.add(new_user)
            db.session.flush()
            # 新建用户登陆方式
            new_user_login = UserLoginMethod(user_id=new_user.id,
                                             login_method="user_name",
                                             identification=user_name,
                                             access_code=passwd)
            db.session.add(new_user_login)
            db.session.commit()
        except Exception as e:
            print(e)
            logger.error(f"password_register error: {e}")
            return None

        data = dict(id=new_user.id, name=user_name)
        print('========:', data)
        return data
