import yaml


def read_yaml(config_name, config_path):
    """
    config_name: configuration content to read
    config_path: configuration file path
    """
    if config_name and config_path:
        with open(config_path, 'r', encoding='utf-8') as f:
            conf = yaml.safe_load(f.read())
        if config_name in conf.keys():
            return conf[config_name.upper()]
        else:
            raise KeyError('No corresponding configuration information found')
    else:
        raise ValueError('Please enter the correct configuration name or configuration file path')