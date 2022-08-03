#!/usr/bin/python3
"""
Applying Unit Test for Amenity Class
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import os


class Test_State(unittest.TestCase):
    """ Testing Amenity class """

    def test_file_exists(self):
        os.path.isfile("../../models/amenity.py")

    def test_issubclass(self):
        """ BaseModel / subclass """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attrs(self):
        """ attr check """
        self.assertTrue('name' in Amenity.__dict__)

    def test_data_types(self):
        """ data types check """
        amenity = Amenity()
        self.assertTrue(type(amenity.name), str)

    def test_values(self):
        """ values check """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_str(self):
        """ str check """
        amenity = Amenity()
        string = "[{}] ({}) {}"\
                 .format(Amenity.__name__, amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))

    def test_save(self):
        """ save check """
        amenity = Amenity()
        amenity.save()
        self.assertNotEqual(amenity.created_at, amenity.updated_at)

    def test_to_dict(self):
        """ to dict check """
        amenity = Amenity()
        new_dict = amenity.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue('to_dict' in dir(amenity))

    def test_docstring(self):
        """ docstring check """
        self.assertIsNotNone(Amenity.__doc__)


if __name__ == "__main__":
    unittest.main()
