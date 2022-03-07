#!/usr/bin/python3
"""Unittests for State class"""
from unittest import result
from models.base_model import BaseModel
from models.state import State
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
import json
import os

"""TestState class that inherits from unittest.Testcase class"""


class TestState(unittest.TestCase):
    def setUp(self):
        """Method to create an instance for each test"""
        self.my_state = State()

    def tearDown(self):
        """Method to delete the instance afeter each test"""
        try:
            os.remove("file.json")
            del self.my_state
        except Exception:
            pass

    def test_State(self):
        """Test for State class"""
        state_name = "Antioquia"
        self.my_state.name = "Antioquia"

        self.assertIsInstance(self.my_state, BaseModel)
        self.assertEqual(self.my_state.name, state_name)
        self.assertEqual(type(self.my_state.name), type(state_name))


if __name__ == '__main__':
    unittest.main()
