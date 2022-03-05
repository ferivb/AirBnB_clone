#!/usr/bin/python3
"""Base Model class module"""
from time import strptime
from unicodedata import name
import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines all common attributes/methods
    for other classes"""

    def __init__(self, *args, **kwargs):
        """BaseModel constructor"""

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        format = "%Y-%m-%dT%H:%M:%S.%f"
                        value_format = datetime.strptime(value, format)
                        setattr(self, key, value_format)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        temp_dict = self.__dict__.copy()
        temp_dict["__class__"] = self.__class__.__name__
        temp_dict["created_at"] = self.created_at.isoformat()
        temp_dict["updated_at"] = self.updated_at.isoformat()
        return temp_dict

    def __str__(self):
        """Prints [<class name>] (<self.id>) <self.__dict__>"""
        c_name = self.__class__.__name__
        return "[{}] ({}) {}".format(c_name, self.id, self.__dict__)
