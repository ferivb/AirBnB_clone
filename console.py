#!/bin/python3
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """ class that implements a command interpreter
        with quit, help methods and a custumize prompt
    """
    """Class attribute prompt defined"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def do_create(self, line):
        """ Create command that creates an instance of BaseModel,
            saves it and prints the id
        """
        if len(line) == 0:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            inst = BaseModel()
            print(inst.id)
            inst.save()

    def do_show(self, line):
        """ Show command that prints the string representation
            of an instance based on the class name and id
        """
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg) != 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key in all_objects.keys():
                print(all_objects[key])
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
