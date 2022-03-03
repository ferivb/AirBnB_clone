#!/usr/bin/python3
from models.base_model import BaseModel
import json


class FileStorage:
    """Serializes instances to a JSON file
    and deserializes JSON file to instances

    __objects stores the dicts created by BaseModel
    Objects format: key = <class name>.id
    value = the dict created"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key
        <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        temp_dict = {key: obj}
        FileStorage.__objects.update(temp_dict)

    def save(self):
        """serializes __objects to the
        JSON file (path: __file_path)"""
        correct_dict = {}
        for key, value in self.__objects.items():
            correct_dict.update({key: value.to_dict()})
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(correct_dict, file)

    def reload(self):
        """Deserializes the JSON file to
        __objects (only if the JSON file
        (__file_path) exists"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                diction = json.loads(file.read())
                for key, value in diction.items():
                    temp = BaseModel(**value)
                    FileStorage.__objects[key] = temp
        except Exception:
            pass
