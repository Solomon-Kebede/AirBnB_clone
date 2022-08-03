#!/usr/bin/python3
"""
Applying Unit Test for FileStorage class
"""
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class Test_FileStorage(unittest.TestCase):
    """ Testing FileStorage class """
    def test_classes(self):
        """check if classes are created"""

        self.assertIsInstance(models.engine.file_storage.FileStorage(),
                              models.engine.file_storage.FileStorage)

    def test_all(self):
        """check if all method is working"""

        self.assertIsNotNone(models.engine.file_storage.FileStorage().all)

    def test_new(self):
        """check if new method is working"""

        self.assertIsNotNone(models.engine.file_storage.FileStorage().new)

    def test_save(self):
        """check if save method is working"""

        self.assertIsNotNone(models.engine.file_storage.FileStorage().save)

    def test_reload(self):
        """check if reload method is working"""

        self.assertIsNotNone(models.engine.file_storage.FileStorage().reload)

    def test_all_method(self):
        """check if all method is working"""

        self.assertIsNotNone(models.engine.file_storage.FileStorage().all())

    def test_models_all(self):
        """check if all method is working"""

        self.assertIsNotNone(models.storage.all())

    def setUp(self):
        """ init instance """
        self.my_model = BaseModel()
        self.storage = FileStorage()

    def test_docmodule(self):
        """ checking doc module """
        self.assertGreater(len(models.engine.file_storage.__doc__), 1)

    def test_docclass(self):
        """checking doc class"""
        self.assertGreater(len(models.engine.file_storage.FileStorage.__doc__),
                           1)

    def test_reload(self):
        """ test reload from json """
        self.my_model.name = "My_first_model"
        self.my_model.my_number = 89
        name = str(self.my_model.__class__.__name__)
        key = name + "." + str(self.my_model.id)
        self.my_model.save()
        self.storage.reload()
        objs = self.storage.all()
        self.obj_reload = objs[key]
        self.assertTrue(self.my_model.__dict__ == self.obj_reload.__dict__)
        self.assertTrue(self.my_model is not self.obj_reload)
        self.assertIsInstance(self.obj_reload, BaseModel)
        self.assertTrue(self.storage.all(), "My_first_model")
        self.assertNotEqual(self.obj_reload.created_at,
                            self.obj_reload.updated_at)

    def test_attrd(self):
        """test for presence of attributes"""
        self.assertEqual(dict, type(self.storage.all()))

    def test_doc(self):
        """claass ann method docstrings"""

        self.assertIsNotNone(models.engine.file_storage.FileStorage.__doc__)
        self.assertIsNotNone(models.engine.file_storage.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.
                             all.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.
                             __init__.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.
                             new.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.
                             save.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.
                             reload.__doc__)


if __name__ == "__main__":
    unittest.main()
