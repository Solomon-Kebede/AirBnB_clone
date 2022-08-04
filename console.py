#!/usr/bin/python3
"""
Doc Console Module
"""
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime
from os import system
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """
    Class Doc
    """
    if sys.stdin and sys.stdin.isatty():
        prompt = '(hbnb) '
    else:
        prompt = '(hbnb)\n'

    systemClasses = ['BaseModel', 'User', 'State',
                     'City', 'Amenity', 'Place', 'Review']

    # ----- basic CLI commands ----- #
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_clear(self, arg):
        """Clean Screen"""
        system('clear')

    def emptyline(self):
        """Pass on empty line"""
        pass

    # ----- extended CLI commands ----- #
    def do_create(self, arg):
        """Creates a new instance of BaseModel, \
saves it (to the JSON file) and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            myObject = eval(args[0] + '()')
            myObject.save()
            print(myObject.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of \
an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.systemClasses:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        else:
            try:
                print(storage.all()[args[0] + '.' + args[1]])
            except Exception:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class \
name and id (save the change into the JSON file)."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.systemClasses:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        else:
            key = args[0] + "." + args[1].strip('"')
            try:
                del storage.all()[key]
                storage.save()
            except Exception:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all \
instances based or not on the class name."""
        myObject = storage.all()
        res = []
        if not arg:
            for key, value in myObject.items():
                res.append(str(value))
            if len(res) != 0:
                print("[{0}]".format(
                    ', '.join(map(str, res))))
            return
        args = arg.split()
        if args[0] not in self.systemClasses:
            print("** class doesn't exist **")
            return
        for key, value in myObject.items():
            if args[0] == str(key.split('.')[0]):
                res.append(str(value))
        if len(res) != 0:
            print("[{0}]".format(
                ', '.join(map(str, res))))
        return

    def do_update(self, arg):
        """Updates an instance based on the class name \
and id by adding or updating attribute (save \
the change into the JSON file)."""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing  **")
            return
        elif len(args) == 2:
            print("** attribute name missing  **")
            return
        elif len(args) == 3:
            print("** value missing  **")
            return
        elif args[0] not in self.systemClasses:
            print("** class doesn't exist **")
            return
        else:
            classId = args[0] + "." + args[1].strip('"')
            myObject = models.storage.all()

            try:
                setAttr = args[2].strip('"')
                setAttrValue = args[3].strip('"')
                setattr(myObject[classId], setAttr, setAttrValue)
                models.storage.save()
                return

            except Exception:
                print("** no instance found **")
                return

    def __update_from_dict(self, mod_class, id, arg):
        """update an instance based on his ID with a dictionary"""
        classId = mod_class + "." + id
        myObject = models.storage.all()
        try:
            for key, value in arg.items():
                if key == "id":
                    continue
                if key == "created_at":
                    myObject[classId]["created_at"] = datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                    continue
                if key == "updated_at":
                    myObject[classId]["updated_at"] = datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                    continue
                if key == '__class__':
                    continue
                setAttr = key
                setAttrValue = value
                setattr(myObject[classId], setAttr, setAttrValue)
            models.storage.save()
        except Exception:
            pass
        return

    def __dict_builder(self, arg):
        """
        private: builds dictionary from string if it is
        allowed by string's proper articulation
        """
        if '{' and '}' in arg:
            tmp = arg.split('}', 1)
            if tmp[1] == '':
                tmp = tmp[0].split('{', 1)[1]
                tmp = tmp.split(', ')
                tmp = list(couple.split(':') for couple in tmp)
                d = {}
                for sub_list in tmp:
                    k = sub_list[0].strip('"\' {}')
                    v = sub_list[1].strip('"\' {}')
                    d[k] = v
                return d
            else:
                return None
        else:
            return None

    def precmd(self, arg):
        """Parser for inputs of the kind <ClassName>.command\n"""
        if arg and ('(' and ')' and '.' in arg):
            args = arg.split('.', 1)
            if args[0] != '' and args[1] != '':
                mod_class = args[0].strip('"')
                args = args[1].split('(', 1)
                if args[0] != '' and args[1] != '':
                    cmnd = args[0]
                    args = args[1].split(')', 1)
                    if args[1] == '':
                        attr_name = ''
                        attr_value = ''
                        if ',' in args[0]:
                            args = args[0].split(',', 1)
                            id = args[0].strip('"')
                            if args[1] != '':
                                d = self.__dict_builder(args[1])
                                if d is not None:
                                    self.__update_from_dict(mod_class, id, d)
                                    line = 'show'+' ' + mod_class+' ' + id
                                    return line
                                else:
                                    if ',' in args[1]:
                                        args = args[1].split(',')
                                    else:
                                        return arg
                            if len(args) == 2:
                                attr_name = args[0].strip('"')
                                attr_value = args[1].strip('"')
                        else:
                            id = args[0].strip('"')
                        line = cmnd + ' ' + mod_class + ' ' \
                            + id + ' ' + attr_name + ' ' + attr_value
                        try:
                            return line
                        except Exception:
                            return arg
                    else:
                        return arg
                else:
                    return arg
            else:
                return arg
        else:
            return arg

    def do_count(self, arg):
        """Retrieves the number of instances of a class"""
        instancesNumber = 0
        myObject = models.storage.all()

        if not arg:
            for key in myObject.keys():
                instancesNumber += 1

        else:
            if arg in self.systemClasses:
                for key in myObject.keys():
                    classId = key.split(".")
                    if classId[0] == arg:
                        instancesNumber += 1
            else:
                print("** class doesn't exist **")
                return

        print(instancesNumber)
        return

    def do_stats(self, arg):
        """Returns an object with the number of instances for each class"""
        myObject = models.storage.all()
        myStats = {}

        if not arg:
            for key in myObject.keys():
                classId = key.split(".")
                if classId[0] not in myStats:
                    myStats.update({"{}".format(classId[0]): 1})
                else:
                    myStats[classId[0]] += 1
            print(myStats)
            return

        else:
            print("** no args allowed for this method **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
