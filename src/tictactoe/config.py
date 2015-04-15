# config.py
import os

class Configuration(object):
    _FOLDER = os.path.dirname(os.path.realpath(__file__))
    CONFIG_FILE_PATH = os.path.join(_FOLDER,"../../","config/config.xml")

    def __init__(self):
        
        if not os.path.exists(self.CONFIG_FILE_PATH):
            raise ConfigFileNotFoundError("ConfigXML does not exist")


class ConfigFileNotFoundError(Exception):
    pass
