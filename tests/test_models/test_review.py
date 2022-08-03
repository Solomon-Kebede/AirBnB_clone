#!/usr/bin/python3
"""
Applying Unit Test for Review Class
"""
import unittest
from models.base_model import BaseModel
from models.review import Review
import os


class Test_Review(unittest.TestCase):
    """ Testing Review class """

    def test_file_exists(self):
        os.path.isfile("../../models/review.py")

    def test_issubclass(self):
        """ BaseModel / subclass """
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attrs(self):
        """ attr check """
        self.assertTrue('place_id' in Review.__dict__)
        self.assertTrue('user_id' in Review.__dict__)
        self.assertTrue('text' in Review.__dict__)

    def test_data_types(self):
        """ data types check """
        review = Review()
        self.assertTrue(type(review.place_id), str)
        self.assertTrue(type(review.user_id), str)
        self.assertTrue(type(review.text), str)

    def test_values(self):
        """ values check """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_str(self):
        """ str check """
        review = Review()
        string = "[{}] ({}) {}"\
                 .format(Review.__name__, review.id, review.__dict__)
        self.assertEqual(string, str(review))

    def test_save(self):
        """ save check """
        review = Review()
        review.save()
        self.assertNotEqual(review.created_at, review.updated_at)

    def test_to_dict(self):
        """ to dict check """
        review = Review()
        new_dict = review.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue('to_dict' in dir(review))

    def test_docstring(self):
        """ docstring check """
        self.assertIsNotNone(Review.__doc__)


if __name__ == "__main__":
    unittest.main()
