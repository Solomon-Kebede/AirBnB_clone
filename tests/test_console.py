#!/usr/bin/python3
"""
testing class console
"""
import console
from console import HBNBCommand
import unittest
from io import StringIO
from unittest.mock import patch
from models import storage


class test_class_base(unittest.TestCase):
    """class for testing class base model"""
    def test_docmodule(self):
        """checking doc module"""
        self.assertIsNotNone(console.__doc__)

    def test_docclass(self):
        """checking doc class"""
        self.assertIsNotNone(HBNBCommand.__doc__)


class Test_console_prompt(unittest.TestCase):
    """ prompt test """
    def test_prompt_string(self):
        """ prompt test """
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_ine(self):
        """ prompt test """
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", f.getvalue().strip())


class Test_console_exit(unittest.TestCase):
    """ quit test """

    def test_exit_exit(self):
        with patch("sys.stdout", new=StringIO()) as output:
            pass

    def test_exit_EOF(self):
        with patch("sys.stdout", new=StringIO()) as output:
            pass


class Test_Console_help(unittest.TestCase):
    """  help test """
    def test_help_quit(self):
        """  help test """
        help = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_EOF(self):
        """  help test """
        help = "EOF command to exit the program"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_create(self):
        """  help test """
        help = ("Creates a new instance of BaseModel, saves it "
                "(to the JSON file) and prints the id.")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_all(self):
        """  help test """
        help = ("Prints all string representation of all instances "
                "based or not on the class name.")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_show(self):
        """  help test """
        help = ("Prints the string representation of an instance "
                "based on the class name and id.")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_destroy(self):
        """  help test """
        help = ("Deletes an instance based on the class name "
                "and id (save the change into the JSON file).")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_count(self):
        """  help test """
        help = ("Retrieves the number of instances of a class")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_update(self):
        """  help test """
        help = ("Updates an instance based on the class name and id by "
                "adding or updating attribute (save the "
                "change into the JSON file).")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help(self):
        """  help test """
        help = ("Documented commands (type help <topic>):\n"
                "========================================\n"
                "EOF  all  clear  count  create  destroy  "
                "help  quit  show  stats  update")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(help, f.getvalue().strip())

    def test_cmd(self):
        """  help cmd """
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", f.getvalue().strip())

    def test_commandobject(self):
        """  help cmd """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Review.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "City.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Amenity.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Place.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "User.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "State.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())


if __name__ == "__main__":
    unittest.main()
