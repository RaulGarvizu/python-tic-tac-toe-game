# config.py

class Configuration(object):
	def __init__(self):
		raise ConfigFileNotFoundError("ConfigXML does not exist")

class ConfigFileNotFoundError(Exception):
	pass