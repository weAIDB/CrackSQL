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


def find_config_file(filename, search_paths=None):
    """
    Intelligently find configuration file
    Search for configuration file in multiple locations in priority order
    
    :param filename: Configuration file name
    :param search_paths: Additional search paths
    :return: Found configuration file path, returns None if not found
    """
    if search_paths is None:
        search_paths = []
        
    # Get the directory where the current module is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    package_dir = os.path.dirname(current_dir)
    
    # Try to get the site-packages directory
    site_packages = None
    for path in sys.path:
        if 'site-packages' in path:
            site_packages = path
            break
    
    # Define search path priority
    paths_to_search = [
        # 1. User specified search paths
        *search_paths,
        
        # 2. Current working directory
        os.path.join(os.getcwd(), filename),
        os.path.join(os.getcwd(), 'config', filename),
        
        # 3. Project directory
        os.path.join(package_dir, filename),
        os.path.join(package_dir, 'config', filename),
        
        # 4. Package installation directory - more combinations
        os.path.join(current_dir, 'config', filename),
    ]
    
    # If site-packages directory is found, add more search paths
    if site_packages:
        paths_to_search.extend([
            os.path.join(site_packages, 'cracksql', filename),
            os.path.join(site_packages, 'cracksql', 'config', filename),
            os.path.join(site_packages, 'cracksql', 'backend', 'config', filename),
            os.path.join(site_packages, 'config', filename),
        ])
    
    # Add system paths
    paths_to_search.extend([
        os.path.join(sys.prefix, 'cracksql', 'config', filename),
        os.path.join('/etc/cracksql', filename),
    ])
    
    # Search all possible paths
    for path in paths_to_search:
        if os.path.exists(path):
            return path
    
    return None


def create_app(config_name='PRODUCTION', config_path=None):
    """
    Create Flask application instance
    :param config_name: Configuration name, defaults to PRODUCTION
    :param config_path: Configuration file path, if None, automatically finds it
    :return: Flask application instance
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

    # Load configuration file
    if config_path is None:
        config_path = find_config_file('config.yaml')
        if config_path is None:
            print("Warning: Unable to find configuration file, using default configuration path")
            config_path = './config/config.yaml'
        print(f"Using configuration file: {config_path}")

    # Load configuration
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            config_data = yaml.safe_load(f)
            if config_name in config_data:
                app.config.update(config_data[config_name])
            else:
                print(f"Warning: Configuration {config_name} not found in configuration file")
    else:
        print(f"Warning: Configuration file does not exist: {config_path}")
        
    # Dynamically set database path
    # Use user execution directory
    current_dir = Path.cwd()
    instance_dir = current_dir / 'instance'
    logs_dir = current_dir / 'logs'
    # Ensure directory exists
    instance_dir.mkdir(exist_ok=True)
    logs_dir.mkdir(exist_ok=True)
    
    # Set database file path
    db_path = instance_dir / 'info.db'
    print(f"Using database: {db_path}")
    
    # Update database URI - using as_uri() to get the correct format for SQLAlchemy
    db_uri = db_path.as_uri().replace('file:', '')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite://{db_uri}'

    # Load logging configuration
    logging_config_path = app.config.get('LOGGING_CONFIG_PATH')
    if logging_config_path:
        logging_config_path = find_config_file(os.path.basename(logging_config_path))
        if logging_config_path and os.path.exists(logging_config_path):
            print(f"Found configuration file: {logging_config_path}")
            with open(logging_config_path, 'r', encoding='utf-8') as f:
                logging_config = yaml.safe_load(f)
                logging.config.dictConfig(logging_config)

    # Load message configuration
    msg_config_path = app.config.get('RESPONSE_MESSAGE')
    if msg_config_path:
        msg_config_path = find_config_file(os.path.basename(msg_config_path))
        if msg_config_path and os.path.exists(msg_config_path):
            print(f"Found configuration file: {msg_config_path}")
            with open(msg_config_path, 'r', encoding='utf-8') as f:
                msg_config = yaml.safe_load(f)
                app.config['RESPONSE_MESSAGE'] = msg_config

    # Initialize database
    db.app = app
    db.init_app(app)
    Migrate(app, db)

    # Register API
    register_api(app, router)

    # Initialize cache
    cache.init_app(app, config={
        "DEBUG": app.config['DEBUG'],
        "CACHE_TYPE": "simple",
        "CACHE_DEFAULT_TIMEOUT": 300
    })

    # Start scheduled tasks
    if app.config.get("SCHEDULER_OPEN"):
        scheduler_init(app)
    
    # Push application context
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
                # If no service name, default to lowercase class name
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
