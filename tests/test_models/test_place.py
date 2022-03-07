#!/usr/bin/python3
"""Unittests for Place class"""
from unittest import result
from models.base_model import BaseModel
from models.place import Place
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
import json
import os

"""TestPlace class that inherits from unittest.Testcase class"""


class TestPlace(unittest.TestCase):
    def setUp(self):
        """Method to create an instance for each test"""
        self.my_place = Place()

    def tearDown(self):
        """Method to delete the instance afeter each test"""
        try:
            os.remove("file.json")
            del self.my_place
        except Exception:
            pass

    def test_Place(self):
        """Test for Place class"""
        city_id = "123"
        self.my_place.city_id = "123"
        user_id = "321"
        self.my_place.user_id = "321"
        name = "Belen"
        self.my_place.name = "Belen"
        description = "Lovely place with excelent view"
        self.my_place.description = "Lovely place with excelent view"
        number_rooms = 3
        self.my_place.number_rooms = 3
        number_bathrooms = 2
        self.my_place.number_bathrooms = 2
        price_by_night = 50
        self.my_place.price_by_night = 50
        latitude = 5.5
        self.my_place.latitude = 5.5
        longitude = 6.0
        self.my_place.longitude = 6.0
        amenity_ids = []

        self.assertIsInstance(self.my_place, BaseModel)
        self.assertEqual(self.my_place.city_id, city_id)
        self.assertEqual(self.my_place.user_id, user_id)
        self.assertEqual(self.my_place.name, name)
        self.assertEqual(self.my_place.description, description)
        self.assertEqual(self.my_place.number_rooms, number_rooms)
        self.assertEqual(type(self.my_place.number_rooms), type(number_rooms))
        self.assertEqual(self.my_place.number_bathrooms, number_bathrooms)
        self.assertEqual(self.my_place.price_by_night, price_by_night)
        self.assertEqual(self.my_place.latitude, latitude)
        self.assertEqual(type(self.my_place.latitude), type(latitude))
        self.assertEqual(self.my_place.longitude, longitude)
        self.assertEqual(type(self.my_place.amenity_ids), type(amenity_ids))


if __name__ == '__main__':
    unittest.main()
