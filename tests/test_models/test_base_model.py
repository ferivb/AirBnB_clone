#!/usr/bin/python3
"""Unittests for BaseModel class"""
from unittest import result
from models.base_model import BaseModel
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
import json
import os

"""module that contains unittests for BaseModel class"""

"""TestBaseModel class that inherits from unittest.Testcase class"""


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Method to create an instance for each test"""
        self.my_model = BaseModel()

    def tearDown(self):
        """Method to delete file.json afeter each test"""
        try:
            os.remove("file.json")
            del self.my_model
        except Exception:
            pass

    def test_to_dict(self):
        """Test for to_dict method"""
        test_dict = {}
        test_dict["id"] = self.my_model.id
        created_at = self.my_model.created_at.isoformat()
        updated_at = self.my_model.updated_at.isoformat()
        test_dict["created_at"] = created_at
        test_dict["updated_at"] = updated_at
        test_dict["__class__"] = "BaseModel"

        self.assertEqual(test_dict, self.my_model.to_dict())

    def test_save(self):
        """Test for save method"""
        updated_at_1 = self.my_model.updated_at
        print(updated_at_1)
        self.my_model.save()
        updated_at_2 = self.my_model.updated_at
        print(updated_at_2)

        self.assertNotEqual(updated_at_1, updated_at_2)

    def test__str__(self):
        """Tests for __str__ method"""
        strmodel = self.my_model.__str__()
        
        self.assertTrue(hasattr(BaseModel, "__str__"), True)
        self.assertEqual(type(strmodel), str)


if __name__ == '__main__':
    unittest.main()