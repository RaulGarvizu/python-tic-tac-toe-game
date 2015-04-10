# test_configuration.py
import sys
sys.path.append("../src")
import unittest
from tictactoe.config import Configuration, ConfigFileNotFoundError 

class Test_Configuration (unittest.TestCase):
	def test_config_file_should_exist(self):
		try:
			conf = Configuration()
			self.fail("Configuration file does not exist constructor will fail")
		except ConfigFileNotFoundError, e:
			pass
	
if __name__ == '__main__':
	unittest.main()
