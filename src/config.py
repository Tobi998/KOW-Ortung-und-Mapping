"""
This file conmtains functions to create and load configurations
"""

import configparser

def load_config(path, dir_name, name):
    """
    Load a single config value from the config file
    """

    config = configparser.ConfigParser()
    config.read(path)
    return config[dir_name][name]

def load_config_bool(path, dir_name, name):
    """
    Load a single config value from the config file
    """

    config = configparser.ConfigParser()
    config.read(path)
    return config.getboolean(dir_name, name)

def create_default_config():
    """
    Creates a config file with default values
    """

    config = configparser.ConfigParser()

    config['DEFAULT'] = {
        "ODOMETER_TO_MM_FACTOR" : 1.9,
        "Radius_mm" : [ 295.4, 360, 0,-360, -295.4],
        "Hall_mv" : [2671, 2640, 2570, 2511, 2490],
        "interp_kind" : "linear"
    }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)


