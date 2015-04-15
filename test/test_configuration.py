# test_configuration.py

import sys
import os
sys.path.append("../src")

import unittest
from tictactoe.config import Configuration, ConfigFileNotFoundError 

class Test_Configuration (unittest.TestCase):

    TEST_PATH = os.path.realpath(__file__)
    TEST_FOLDER = os.path.dirname(TEST_PATH)
    CONFIG_FILE_PATH = os.path.join(TEST_FOLDER,"../","config/config.xml")

    def test_config_file_should_exist(self):

        self.delete_config_file()
        try:
            conf = Configuration()
            self.fail("Configuration file does not exist constructor will fail")
        except ConfigFileNotFoundError, e:
            pass

    def test_configuration_can_be_created_if_config_file_exist(self):
        self.create_config_file()
        conf = Configuration()
        self.assertTrue(isinstance(conf, Configuration))


    def delete_config_file(self):        
        if os.path.exists(self.CONFIG_FILE_PATH):
            os.unlink(self.CONFIG_FILE_PATH)

    def create_config_file(self):        
        open(self.CONFIG_FILE_PATH, 'a').close()


if __name__ == '__main__':
    unittest.main()
