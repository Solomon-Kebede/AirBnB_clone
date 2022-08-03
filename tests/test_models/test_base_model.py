#!/usr/bin/python3
"""
Applying Unit Test for BaseModel Class
"""
import unittest
from models.base_model import BaseModel
from models import base_model
import inspect
import pycodestyle
import os
from datetime import datetime
from time import sleep


class Test_Docs_BaseModel(unittest.TestCase):
    """Class for testing docs in BaseModel"""

    all_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_file_exists(self):
        os.path.isfile("../../models/base_model.py")

    def test_doc_file(self):
        """check for documentation"""
        expected = "\nBaseModel Class (Models' module)\n"
        actual = base_model.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """check documentation for the class"""
        expected = "defines the abstract class BaseModel"
        actual = BaseModel.__doc__
        self.assertEqual(expected, actual)

    def test_all_function_docs(self):
        """check for documentation in all functions"""
        all_functions = Test_Docs_BaseModel.all_funcs
        for function in all_functions:
            self.assertIsNotNone(function[1].__doc__)

    def test_pep8_base_model(self):
        """checks base_model.py conforms to pycode Style"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        errors = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_file_is_executable(self):
        """checks executability"""
        file_stat = os.stat('models/base_model.py')
        permissions = str(oct(file_stat[0]))
        actual = int(permissions[5:-2]) >= 5
        self.assertTrue(actual)


class Test_Init_BaseModel_1(unittest.TestCase):
    """Testing instances and variables thereof"""

    def setUp(self):
        """new instance for each individual testing"""
        self.model = BaseModel()

    def test_instance_generation(self):
        """checks proper instantiation"""
        self.assertIsInstance(self.model, BaseModel)

    def test_save(self):
        """check save function should add updated_at attribute"""
        self.model.save()
        actual = type(self.model.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    def test_to_string(self):
        """checks if BaseModel is casted to string"""
        my_str = str(self.model)
        my_list = ['BaseModel', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_id_evolution(self):
        """checks for a reasonable id evolution"""
        test_a = BaseModel()
        test_b = BaseModel()
        self.assertTrue(test_a.id != test_b.id)


class Test_init_BaseModel_2(unittest.TestCase):
    """ Test BaseModel Init """

    def test_BaseModel_init(self):
        """ Test BaseModel """
        self.assertTrue(hasattr(BaseModel(), "id"))
        self.assertTrue(hasattr(BaseModel(), "created_at"))
        self.assertTrue(hasattr(BaseModel(), "updated_at"))

    def test_BaseModel_init_noargs(self):
        """ Test BaseModel with no args """
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_BaseModel_created_at_1(self):
        """ Test created_at_1 """
        self.assertTrue(isinstance(BaseModel().created_at, datetime))

    def test_BaseModel_created_date_2(self):
        """ Test created_at_2 """
        self.assertEqual(type(BaseModel().created_at), datetime)

    def test_BaseModel_updated_at_1(self):
        """ test updated_at_1 """
        self.assertTrue(isinstance(BaseModel().updated_at, datetime))

    def test_BaseModel_updated_at_2(self):
        """ test updated_at_2 """
        self.assertEqual(type(BaseModel().updated_at), datetime)

    def test_BaseModel_create_sleep(self):
        """ create two objects at different time """
        baseModel1 = BaseModel()
        sleep(1)
        baseModel2 = BaseModel()
        self.assertNotEqual(baseModel1.created_at, baseModel2.created_at)


class Test_Save_BaseModel(unittest.TestCase):
    """ Test BaseModel Save """

    def test_BaseModel_save_1(self):
        """ Test save """
        baseModel = BaseModel()
        baseModel.save()
        self.assertNotEqual(baseModel.created_at, baseModel.updated_at)

    def test_BaseModel_save_2(self):
        """ Test save twice """
        baseModel = BaseModel()
        baseModel.save()
        sleep(1)
        baseModel.save()
        self.assertLess(baseModel.created_at, baseModel.updated_at)


class Test_To_Dict_BaseModel(unittest.TestCase):
    """ Test BaseModel to_dict """

    def test_BaseModel_dict_keys(self):
        """ Test to_dict correct keys """
        baseModel = BaseModel()
        self.assertIn("id", baseModel.to_dict())
        self.assertIn("created_at", baseModel.to_dict())
        self.assertIn("updated_at", baseModel.to_dict())
        self.assertIn("__class__", baseModel.to_dict())


class Test_Str_BaseModel(unittest.TestCase):
    """ Test BaseModel str """

    def test_BaseModel_str(self):
        """ Test str """
        baseModel = BaseModel()
        self.assertEqual(type(str(baseModel)), str)

    def test_BaseModel_add_attr(self):
        """ test to_dict """
        baseModel = BaseModel()
        baseModel.name = "Holberton"
        baseModel.my_number = 92047291
        self.assertIn("name", baseModel.to_dict())
        self.assertIn("my_number", baseModel.to_dict())

    def test_BaseModel_format_date(self):
        """ Test date format """
        baseModel = BaseModel()
        self.assertEqual(type(baseModel.to_dict()["created_at"]), str)
        self.assertEqual(type(baseModel.to_dict()["updated_at"]), str)

    def test_BaseModel_list_type(self):
        """ Test to_dict """
        baseModel = BaseModel()
        self.assertEqual(type(baseModel.to_dict()), dict)

    def test_BaseModel_dict_values(self):
        """ Test to_dict """
        baseModel = BaseModel()
        self.assertEqual(type(baseModel.to_dict()["id"]), str)
        self.assertEqual(type(baseModel.to_dict()["created_at"]), str)
        self.assertEqual(type(baseModel.to_dict()["updated_at"]), str)
        self.assertEqual(type(baseModel.to_dict()["__class__"]), str)

    def test_BaseModel_full_dict(self):
        """ test to_dict """
        baseModel = BaseModel()
        baseModel.name = "Holberton"
        baseModel.my_number = 92047291
        self.assertEqual(type(baseModel.to_dict()), dict)
        self.assertIn("name", baseModel.to_dict())
        self.assertIn("my_number", baseModel.to_dict())
        self.assertIn("id", baseModel.to_dict())
        self.assertIn("created_at", baseModel.to_dict())
        self.assertIn("updated_at", baseModel.to_dict())
        self.assertIn("__class__", baseModel.to_dict())


if __name__ == "__main__":
    """TEST BaseModel"""
    unittest.main()
