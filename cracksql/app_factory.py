import os
import yaml
import logging
import logging.config
from flask import Flask, Blueprint
from flask_cors import CORS
from flask_migrate import Migrate
from api.utils.core import JSONEncoder
from api.utils.scheduler import scheduler_init
from api.router import router
from config.db_config import db
import models  # Can not be deleted, used for flask_migrate ！！！
from config.cache import cache
from utils.public import read_yaml


def create_app(config_name, config_path=None):
    app = Flask(__name__)

    CORS(
        app,
        supports_credentials=True,
        resources=r'/*',
        expose_headers=[
            'Origin',
            'Accept',
            'Content-Type',
            'Content-Disposition',
            'Access-Control-Allow-Origin'])

    # Read configuration file
    if not config_path:
        pwd = os.getcwd()
        config_path = os.path.join(pwd, 'config/config.yaml')
    if not config_name:
        config_name = 'PRODUCTION'

    # Read configuration file
    conf = read_yaml(config_name, config_path)
    app.config.update(conf)

    # Register interfaces
    register_api(app=app, routers=router)

    # Return JSON format conversion
    app.json_encoder = JSONEncoder

    # Log file directory
    if not os.path.exists(app.config['LOGGING_PATH']):
        os.mkdir(app.config['LOGGING_PATH'])

    # Log settings
    with open(app.config['LOGGING_CONFIG_PATH'], 'r', encoding='utf-8') as f:
        dict_conf = yaml.safe_load(f.read())
    logging.config.dictConfig(dict_conf)

    # Read msg configuration
    with open(app.config['RESPONSE_MESSAGE'], 'r', encoding='utf-8') as f:
        msg = yaml.safe_load(f.read())
        app.config.update(msg)

    # Register database connection
    db.app = app
    db.init_app(app)
    Migrate(app, db)

    # Cache
    cache.init_app(app, {
        "DEBUG": app.config['DEBUG'],
        "CACHE_TYPE": "simple",
        "CACHE_DEFAULT_TIMEOUT": 300
    })

    # Start scheduled tasks
    if app.config.get("SCHEDULER_OPEN"):
        scheduler_init(app)

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
