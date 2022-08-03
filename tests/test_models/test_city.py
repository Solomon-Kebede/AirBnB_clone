#!/usr/bin/python3
"""
Applying Unit Test for City Class
"""
import unittest
from models.base_model import BaseModel
from models.city import City
import os


class Test_City(unittest.TestCase):
    """ Testing City class """

    def test_file_exists(self):
        os.path.isfile("../../models/city.py")

    def test_issubclass(self):
        """ BaseModel / subclass """
        self.assertTrue(issubclass(City, BaseModel))

    def test_attrs(self):
        """ attr check """
        self.assertTrue('state_id' in City.__dict__)
        self.assertTrue('name' in City.__dict__)

    def test_data_types(self):
        """ data types check """
        city = City()
        self.assertTrue(type(city.state_id), str)
        self.assertTrue(type(city.name), str)

    def test_values(self):
        """ values check """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_str(self):
        """ str check """
        city = City()
        string = "[{}] ({}) {}"\
                 .format(City.__name__, city.id, city.__dict__)
        self.assertEqual(string, str(city))

    def test_save(self):
        """ save check """
        city = City()
        city.save()
        self.assertNotEqual(city.created_at, city.updated_at)

    def test_to_dict(self):
        """ to dict check """
        city = City()
        new_dict = city.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue('to_dict' in dir(city))

    def test_docstring(self):
        """ docstring check """
        self.assertIsNotNone(City.__doc__)


if __name__ == "__main__":
    unittest.main()
