import os
import yaml
import logging
import logging.config
import sys
import importlib.util
from pathlib import Path
from flask import Flask, Blueprint
from flask_cors import CORS
from flask_migrate import Migrate
from api.utils.core import JSONEncoder
from api.utils.scheduler import scheduler_init
from api.router import router
from config.db_config import db
from models import *  # Can not be deleted, used for flask_migrate ！！！
from config.cache import cache
from utils.public import read_yaml


def is_package_installed(package_name):
    """
    检查指定的包是否已安装
    
    :param package_name: 包名
    :return: 如果包已安装返回 True，否则返回 False
    """
    try:
        spec = importlib.util.find_spec(package_name)
        return spec is not None
    except (ImportError, AttributeError):
        return False


def get_user_data_path(filename=None, app_name="CrackSQL"):
    """
    获取用户数据目录中的文件路径
    
    :param filename: 文件名，如果为 None，则返回目录路径
    :param app_name: 应用名称
    :return: 文件路径
    """
    # 获取用户主目录
    home = Path.home()
    
    # 根据操作系统选择合适的数据目录
    if sys.platform == "win32":
        # Windows
        data_dir = home / "AppData" / "Local" / app_name
    elif sys.platform == "darwin":
        # macOS
        data_dir = home / "Library" / "Application Support" / app_name
    else:
        # Linux 和其他类 Unix 系统
        data_dir = home / ".local" / "share" / app_name
    
    # 确保目录存在
    data_dir.mkdir(parents=True, exist_ok=True)
    
    # 如果指定了文件名，则返回文件路径
    if filename:
        return str(data_dir / filename)
    
    # 否则返回目录路径
    return str(data_dir)


def find_config_file(filename, search_paths=None):
    """
    智能查找配置文件
    按照优先级顺序在多个位置查找配置文件
    
    :param filename: 配置文件名
    :param search_paths: 额外的搜索路径
    :return: 找到的配置文件路径，如果未找到则返回None
    """
    if search_paths is None:
        search_paths = []
        
    # 获取当前模块所在的目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    package_dir = os.path.dirname(current_dir)
    
    # 尝试获取site-packages目录
    site_packages = None
    for path in sys.path:
        if 'site-packages' in path:
            site_packages = path
            break
    
    # 定义搜索路径优先级
    paths_to_search = [
        # 1. 用户指定的搜索路径
        *search_paths,
        
        # 2. 当前工作目录
        os.path.join(os.getcwd(), filename),
        os.path.join(os.getcwd(), 'config', filename),
        
        # 3. 项目目录
        os.path.join(package_dir, filename),
        os.path.join(package_dir, 'config', filename),
        
        # 4. 包安装目录 - 更多的组合
        os.path.join(current_dir, 'config', filename),
    ]
    
    # 如果找到了site-packages目录，添加更多的搜索路径
    if site_packages:
        paths_to_search.extend([
            os.path.join(site_packages, 'cracksql', filename),
            os.path.join(site_packages, 'cracksql', 'config', filename),
            os.path.join(site_packages, 'cracksql', 'backend', 'config', filename),
            os.path.join(site_packages, 'config', filename),
        ])
    
    # 添加系统路径
    paths_to_search.extend([
        os.path.join(sys.prefix, 'cracksql', 'config', filename),
        os.path.join('/etc/cracksql', filename),
    ])
    
    # 搜索所有可能的路径
    for path in paths_to_search:
        if os.path.exists(path):
            return path
    
    return None


def create_app(config_name='PRODUCTION', config_path=None):
    """
    创建Flask应用实例
    :param config_name: 配置名称，默认为PRODUCTION
    :param config_path: 配置文件路径，如果为None则自动查找
    :return: Flask应用实例
    """
    
    app = Flask(__name__)

    CORS(
        app,
        supports_credentials=True,
        resources=r'/*',
        expose_headers=[
            'Origin',
            'Accept',
            'Content-Type',
            'Content-Length',
            'Accept-Language',
            'Accept-Encoding',
            'Cookie',
            'Recent-Activity',
            'Authorization',
            'X-CSRF-TOKEN',
            'X-Requested-With',
        ]
    )

    # 加载配置文件
    if config_path is None:
        config_path = find_config_file('config.yaml')
        if config_path is None:
            print("警告: 无法找到配置文件，使用默认配置路径")
            config_path = './config/config.yaml'
        print(f"使用配置文件: {config_path}")

    # 加载配置
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            config_data = yaml.safe_load(f)
            if config_name in config_data:
                app.config.update(config_data[config_name])
            else:
                print(f"警告: 配置文件中未找到 {config_name} 配置")
    else:
        print(f"警告: 配置文件不存在: {config_path}")
        
    # 动态设置数据库路径
    # 使用用户执行目录
    current_dir = os.getcwd()
    instance_dir = os.path.join(current_dir, 'instance')
    
    # 确保目录存在
    os.makedirs(instance_dir, exist_ok=True)
    
    # 设置数据库文件路径
    db_path = os.path.join(instance_dir, 'info.db')
    print(f"使用数据库: {db_path}")
    
    # 更新数据库 URI
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////{db_path}'

    # 加载日志配置
    logging_config_path = app.config.get('LOGGING_CONFIG_PATH')
    if logging_config_path:
        logging_config_path = find_config_file(os.path.basename(logging_config_path))
        if logging_config_path and os.path.exists(logging_config_path):
            print(f"找到配置文件: {logging_config_path}")
            with open(logging_config_path, 'r', encoding='utf-8') as f:
                logging_config = yaml.safe_load(f)
                logging.config.dictConfig(logging_config)

    # 加载消息配置
    msg_config_path = app.config.get('RESPONSE_MESSAGE')
    if msg_config_path:
        msg_config_path = find_config_file(os.path.basename(msg_config_path))
        if msg_config_path and os.path.exists(msg_config_path):
            print(f"找到配置文件: {msg_config_path}")
            with open(msg_config_path, 'r', encoding='utf-8') as f:
                msg_config = yaml.safe_load(f)
                app.config['RESPONSE_MESSAGE'] = msg_config

    # 初始化数据库
    db.app = app
    db.init_app(app)
    Migrate(app, db)

    # 注册API
    register_api(app, router)

    # 初始化缓存
    cache.init_app(app, config={
        "DEBUG": app.config['DEBUG'],
        "CACHE_TYPE": "simple",
        "CACHE_DEFAULT_TIMEOUT": 300
    })

    # 启动定时任务
    if app.config.get("SCHEDULER_OPEN"):
        scheduler_init(app)
    
    # 推送应用上下文
    app.app_context().push()

    return app


def register_api(app, routers):
    for router_api in routers:
        if isinstance(router_api, Blueprint):
            app.register_blueprint(router_api)
        else:
            try:
                endpoint = router_api.__name__
                view_func = router_api.as_view(endpoint)
                # 如果没有服务名,默认 类名小写
                if hasattr(router_api, "service_name"):
                    url = '/{}/'.format(router_api.service_name.lower())
                else:
                    url = '/{}/'.format(router_api.__name__.lower())
                if 'GET' in router_api.__methods__:
                    app.add_url_rule(
                        url,
                        defaults={
                            'key': None},
                        view_func=view_func,
                        methods=[
                            'GET',
                        ])
                    app.add_url_rule(
                        '{}<string:key>'.format(url),
                        view_func=view_func,
                        methods=[
                            'GET',
                        ])
                if 'POST' in router_api.__methods__:
                    app.add_url_rule(
                        url, view_func=view_func, methods=[
                            'POST', ])
                if 'PUT' in router_api.__methods__:
                    app.add_url_rule(
                        '{}<string:key>'.format(url),
                        view_func=view_func,
                        methods=[
                            'PUT',
                        ])
                if 'DELETE' in router_api.__methods__:
                    app.add_url_rule(
                        '{}<string:key>'.format(url),
                        view_func=view_func,
                        methods=[
                            'DELETE',
                        ])
            except Exception as e:
                raise ValueError(e)
