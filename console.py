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
    """Dictionary with all the classes and their inits"""
    classes = {
        'BaseModel': BaseModel()
        }

    @staticmethod
    def typecaster(attr):
        """Type casts the attribute passed on
        console"""
        attr = attr.strip('\"')
        if attr.isdecimal():
            return int(attr)
        else:
            try:
                return float(attr)
            except ValueError:
                return str(attr)

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
        arg = line.split()
        if len(line) == 0:
            print("** class name missing **")
        elif arg[0] not in self.classes.keys():
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
        elif arg[0] not in self.classes.keys():
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

    def do_destroy(self, line):
        """ Delete command that deletes an instance based on the class name
            and id
        """
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif len(arg) != 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key in all_objects.keys():
                del all_objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of
        all instances based or not on the class name"""
        arg = line.split()
        if len(arg) > 0 and arg[0] not in self.classes.keys():
            print("** class doesn't exist **")
        else:
            list = []
            all_objects = storage.all()
            for key in all_objects.keys():
                list.append(BaseModel.__str__(all_objects[key]))
            print(list)

    def do_update(self, line):
        """Updates an instance based on the class
        name and id by adding or updating attribute"""
        arg = line.split()
        all_objects = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key not in all_objects.keys():
                print("** no instance found **")
            elif len(arg) < 3:
                print("** attribute name missing **")
            elif len(arg) < 4:
                print("** value missing **")
            else:
                """attr = type(getattr(all_objects[key], arg[2]))"""
                trimmed = HBNBCommand.typecaster(arg[3])
                setattr(all_objects[key], arg[2], trimmed)
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
