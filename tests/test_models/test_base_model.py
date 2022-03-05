#!/usr/bin/python3

from models.base_model import BaseModel
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
import json

"""module that contains unittests for BaseModel class"""

"""TestBaseModel class that inherits from unittest.Testcase class"""


class TestBaseModel(unittest.TestCase):
    
    def test_save(self):
        """Test for save method"""

        my_model = BaseModel()
        test_dict = {}
        test_dict["id"] = my_model.id
        created_at = my_model.created_at.isoformat()
        updated_at = my_model.updated_at.isoformat()
        test_dict["created_at"] = created_at
        test_dict["updated_at"] = updated_at
        test_dict["__class__"] = "BaseModel"
        key = "{}.{}".format(BaseModel.__name__, my_model.id)
        result_dict = {}
        result_dict = {key: test_dict}
        my_model.save()
        try:
            with open("file.json", 'r', encoding='utf-8') as file:
                diction = json.loads(file.read())
        except Exception:
                pass
        
        
        self.assertEqual(result_dict, diction)
