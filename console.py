#!/usr/bin/python3
"""Console class module"""
import cmd
import re
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ class that implements a command interpreter
        with quit, help methods and a custumize prompt
    """

    """Class attributes:
    prompt and a classes dictionary"""
    prompt = "(hbnb) "
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review,
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

    def emptyline(self):
        "handler for the empty line"
        pass

    def do_quit(self, line):
        """Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def do_create(self, line):
        """Create command that creates an instance of BaseModel,
        saves it and prints the id"""
        arg = line.split()
        if len(line) == 0:
            print("** class name missing **")
        elif arg[0] not in self.classes.keys():
            print("** class doesn't exist **")
        else:
            inst = self.classes[arg[0]]()
            print(inst.id)
            inst.save()

    def do_show(self, line):
        """Show command that prints the string representation
        of an instance based on the class name and id"""
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key in all_objects.keys():
                print(all_objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Delete command that deletes an instance based on the class name
        and id"""
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif len(arg) < 2:
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
        if len(arg) == 0:
            list = []
            all_objects = storage.all()
            for key in all_objects.keys():
                list.append(BaseModel.__str__(all_objects[key]))
            print(list)
        else:
            if len(arg) > 0 and arg[0] not in self.classes.keys():
                print("** class doesn't exist **")
            else:
                list = []
                all_objects = storage.all()
                for key in all_objects.keys():
                    if type(all_objects[key]) == self.classes[arg[0]]:
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

    def default(self, arg):
        """Alternative command usage in the mode <class name>.<command>"""
        commands = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
        }
        arg_list = re.split('[.\",() ]+', arg)
        if arg_list[1] not in commands.keys():
            print("** Unknown command try help **")
        else:
            method = commands[arg_list[1]]
            arg_list[1] = arg_list[0]
            del arg_list[0]
            line = ' '.join(arg_list)
            method(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
