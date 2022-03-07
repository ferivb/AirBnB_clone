#!/usr/bin/python3
"""Unittests for City class"""
from unittest import result
from models.base_model import BaseModel
from models.city import City
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
import json
import os

"""TestCity class that inherits from unittest.Testcase class"""


class TestCity(unittest.TestCase):
    def setUp(self):
        """Method to create an instance for each test"""
        self.my_city = City()

    def tearDown(self):
        """Method to delete the instance afeter each test"""
        try:
            os.remove("file.json")
            del self.my_city
        except Exception:
            pass

    def test_City(self):
        """Test for City class"""
        state_id = "123"
        self.my_city.state_id = "123"
        city_name = "Medellin"
        self.my_city.name = "Medellin"

        self.assertIsInstance(self.my_city, BaseModel)
        self.assertEqual(self.my_city.state_id, state_id)
        self.assertEqual(type(self.my_city.state_id), type(state_id))
        self.assertEqual(self.my_city.name, city_name)
        self.assertEqual(type(self.my_city.name), type(city_name))


if __name__ == '__main__':
    unittest.main()
