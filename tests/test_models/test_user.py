#!/usr/bin/python3
"""Unittests for User class"""
from unittest import result
from models.base_model import BaseModel
from models.user import User
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
import json
import os

"""TestBaseModel class that inherits from unittest.Testcase class"""


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Method to create an instance for each test"""
        self.my_user = User()

    def tearDown(self):
        """Method to delete file.json afeter each test"""
        try:
            os.remove("file.json")
            del self.my_user
        except Exception:
            pass

    def test_User(self):
        """Test for User class"""
        email = "leo@ht.co"
        self.my_user.email = "leo@ht.co"
        password = "1234"
        self.my_user.password = "1234"
        first_name = "Leo"
        self.my_user.first_name = "Leo"
        last_name = "Messi"
        self.my_user.last_name = "Messi"

        self.assertIsInstance(self.my_user, BaseModel)
        self.assertIsInstance(self.my_user, User)
        self.assertEqual(self.my_user.email, email)
        self.assertEqual(self.my_user.password, password)
        self.assertEqual(self.my_user.first_name, first_name)
        self.assertEqual(self.my_user.last_name, last_name)


if __name__ == '__main__':
    unittest.main()
