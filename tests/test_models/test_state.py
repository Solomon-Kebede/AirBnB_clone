#!/usr/bin/python3
"""
Applying Unit Test for State Class
"""
import unittest
from models.base_model import BaseModel
from models.state import State
import os


class Test_State(unittest.TestCase):
    """ Testing State class """

    def test_file_exists(self):
        os.path.isfile("../../models/state.py")

    def test_issubclass(self):
        """ BaseModel / subclass """
        self.assertTrue(issubclass(State, BaseModel))

    def test_attrs(self):
        """ attr check """
        self.assertTrue('name' in State.__dict__)

    def test_data_types(self):
        """ data types check """
        state = State()
        self.assertTrue(type(state.name), str)

    def test_values(self):
        """ values check """
        state = State()
        self.assertEqual(state.name, "")

    def test_str(self):
        """ str check """
        state = State()
        string = "[{}] ({}) {}"\
                 .format(State.__name__, state.id, state.__dict__)
        self.assertEqual(string, str(state))

    def test_save(self):
        """ save check """
        state = State()
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)

    def test_to_dict(self):
        """ to dict check """
        state = State()
        new_dict = state.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue('to_dict' in dir(state))

    def test_docstring(self):
        """ docstring check """
        self.assertIsNotNone(State.__doc__)


if __name__ == "__main__":
    unittest.main()
