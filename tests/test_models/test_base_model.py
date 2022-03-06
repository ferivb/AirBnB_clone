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
        """Metod to create an instance for each test"""
        self.my_model = BaseModel()
        self.my_model.save()

    def tearDown(self):
        """Method to delete file.json afeter each test"""
        try:
            os.remove("file.json")
            del self.my_model
        except Exception:
            pass

    def test_save(self):
        """Test for save method"""
        test_dict = {}
        test_dict["id"] = self.my_model.id
        created_at = self.my_model.created_at.isoformat()
        updated_at = self.my_model.updated_at.isoformat()
        test_dict["created_at"] = created_at
        test_dict["updated_at"] = updated_at
        test_dict["__class__"] = "BaseModel"
        key = "{}.{}".format(BaseModel.__name__, self.my_model.id)
        result_dict = {}
        result_dict = {key: test_dict}

        try:
            with open("file.json", 'r', encoding='utf-8') as file:
                diction = json.loads(file.read())
        except Exception:
            pass

        self.assertEqual(result_dict, diction)

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
