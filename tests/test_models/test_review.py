#!/usr/bin/python3
"""Unittests for Review class"""
from unittest import result
from models.base_model import BaseModel
from models.review import Review
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
import json
import os

"""TestBaseModel class that inherits from unittest.Testcase class"""


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Method to create an instance for each test"""
        self.my_review = Review()

    def tearDown(self):
        """Method to delete file.json afeter each test"""
        try:
            os.remove("file.json")
            del self.my_review
        except Exception:
            pass

    def test_Review(self):
        """Test for Review class"""
        place_id = "321"
        self.my_review.place_id = "321"
        user_id = "123"
        self.my_review.user_id = "123"
        text = "Great place"
        self.my_review.text = "Great place"

        self.assertIsInstance(self.my_review, BaseModel)
        self.assertIsInstance(self.my_review, Review)
        self.assertEqual(self.my_review.place_id, place_id)
        self.assertEqual(type(self.my_review.place_id), type(place_id))
        self.assertEqual(self.my_review.user_id, user_id)
        self.assertEqual(self.my_review.text, text)


if __name__ == '__main__':
    unittest.main()
