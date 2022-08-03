#!/usr/bin/python3
"""
Applying Unit Test for Place Class
"""
import unittest
from models.base_model import BaseModel
from models.place import Place
import os


class Test_Place(unittest.TestCase):
    """ Testing Place class """

    def test_file_exists(self):
        os.path.isfile("../../models/place.py")

    def test_issubclass(self):
        """ BaseModel / subclass """
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attrs(self):
        """ attr check """
        self.assertTrue('city_id' in Place.__dict__)
        self.assertTrue('user_id' in Place.__dict__)
        self.assertTrue('name' in Place.__dict__)
        self.assertTrue('description' in Place.__dict__)
        self.assertTrue('number_rooms' in Place.__dict__)
        self.assertTrue('number_bathrooms' in Place.__dict__)
        self.assertTrue('max_guest' in Place.__dict__)
        self.assertTrue('price_by_night' in Place.__dict__)
        self.assertTrue('latitude' in Place.__dict__)
        self.assertTrue('longitude' in Place.__dict__)
        self.assertTrue('amenity_ids' in Place.__dict__)

    def test_data_types(self):
        """ data types check """
        place = Place()
        self.assertTrue(type(place.city_id), str)
        self.assertTrue(type(place.user_id), str)
        self.assertTrue(type(place.name), str)
        self.assertTrue(type(place.description), str)
        self.assertTrue(type(place.number_rooms), int)
        self.assertTrue(type(place.number_bathrooms), int)
        self.assertTrue(type(place.max_guest), int)
        self.assertTrue(type(place.price_by_night), int)
        self.assertTrue(type(place.latitude), float)
        self.assertTrue(type(place.longitude), float)
        self.assertTrue(type(place.amenity_ids), list)

    def test_values(self):
        """ values check """
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_str(self):
        """ str check """
        place = Place()
        string = "[{}] ({}) {}"\
                 .format(Place.__name__, place.id, place.__dict__)
        self.assertEqual(string, str(place))

    def test_save(self):
        """ save check """
        place = Place()
        place.save()
        self.assertNotEqual(place.created_at, place.updated_at)

    def test_to_dict(self):
        """ to dict check """
        place = Place()
        new_dict = place.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue('to_dict' in dir(place))

    def test_docstring(self):
        """ docstring check """
        self.assertIsNotNone(Place.__doc__)


if __name__ == "__main__":
    unittest.main()
