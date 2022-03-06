#!/usr/bin/python3
"""Unittests for Amenity class"""
from unittest import result
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
import json
import os

"""TestAmenity class that inherits from unittest.Testcase class"""


class TestAmenity(unittest.TestCase):
    def setUp(self):
        """Method to create an instance for each test"""
        self.my_amenity = Amenity()

    def tearDown(self):
        """Method to delete the instance afeter each test"""
        try:
            os.remove("file.json")
            del self.my_amenity
        except Exception:
            pass

    def test_Amenity(self):
        """Test for Amenity class"""
        self.my_amenity.name = "pool"
        name = "pool"

        self.assertIsInstance(self.my_amenity, BaseModel)
        self.assertEqual(self.my_amenity.name, name)
        self.assertEqual(type(self.my_amenity.name), type(name))


if __name__ == '__main__':
    unittest.main()
