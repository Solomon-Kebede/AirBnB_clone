#!/usr/bin/python3
"""
Applying Unit Test for User Class
"""
import unittest
from models.base_model import BaseModel
from models.user import User
import os


class Test_User(unittest.TestCase):
    """ Testing User class """

    def test_file_exists(self):
        os.path.isfile("../../models/user.py")

    def test_issubclass(self):
        """ BaseModel / subclass """
        self.assertTrue(issubclass(User, BaseModel))

    def test_attrs(self):
        """ attr check """
        self.assertTrue('first_name' in User.__dict__)
        self.assertTrue('last_name' in User.__dict__)
        self.assertTrue('email' in User.__dict__)
        self.assertTrue('password' in User.__dict__)

    def test_data_types(self):
        """ data types check """
        user = User()
        self.assertTrue(type(user.first_name), str)
        self.assertTrue(type(user.last_name), str)
        self.assertTrue(type(user.email), str)
        self.assertTrue(type(user.password), str)

    def test_values(self):
        """ values check """
        user = User()
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")

    def test_str(self):
        """ str check """
        user = User()
        string = "[{}] ({}) {}"\
                 .format(User.__name__, user.id, user.__dict__)
        self.assertEqual(string, str(user))

    def test_save(self):
        """ save check """
        user = User()
        user.save()
        self.assertNotEqual(user.created_at, user.updated_at)

    def test_to_dict(self):
        """ to dict check """
        user = User()
        new_dict = user.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue('to_dict' in dir(user))

    def test_docstring(self):
        """ docstring check """
        self.assertIsNotNone(User.__doc__)


if __name__ == "__main__":
    unittest.main()
