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

def load_config_all(path):
    """
    Load all config values from the config file at once
    """
    config = configparser.ConfigParser()
    config.read(path)
    odometertomm = config['DEFAULT']['ODOMETER_TO_MM_FACTOR']
    radius_mm = config['DEFAULT']['Radius_mm']
    hall_mv = config['DEFAULT']['Hall_mv']
    preprocces = config['DEFAULT']['Preprocces']

    return odometertomm, radius_mm, hall_mv, preprocces

def create_default_config():
    """
    Creates a config file with default values
    """

    config = configparser.ConfigParser()

    config['DEFAULT'] = {
        "ODOMETER_TO_MM_FACTOR" : 2.9,
        "Radius_mm" : [ 295.4, 360, 0,-360, -295.4],
        "Hall_mv" : [2671, 2640, 2570, 2511, 2490],
        "Preprocces" : "True"
    }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)


