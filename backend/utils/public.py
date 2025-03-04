import yaml
import os
import sys
import importlib.resources


def read_yaml(config_name, config_path):
    """
    config_name: configuration content to read
    config_path: configuration file path
    """
    if config_name and config_path:
        # 首先尝试直接打开指定路径
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                conf = yaml.safe_load(f.read())
        except FileNotFoundError:
            # 如果找不到文件，尝试从包内读取
            try:
                # 获取包的安装路径
                package_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                # 构建相对于包的配置文件路径
                relative_path = os.path.join(package_path, 'config', 'config.yaml')
                
                with open(relative_path, 'r', encoding='utf-8') as f:
                    conf = yaml.safe_load(f.read())
                print(f"使用包内配置文件: {relative_path}")
            except FileNotFoundError:
                raise FileNotFoundError(f"无法找到配置文件: {config_path} 或包内配置")
        
        if config_name in conf.keys():
            return conf[config_name.upper()]
        else:
            raise KeyError('No corresponding configuration information found')
    else:
        raise ValueError('Please enter the correct configuration name or configuration file path')