#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods
    for other classes"""

    def __init__(self):
        """BaseModel constructor"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        temp_dict = self.__dict__.copy()
        temp_dict["__class__"] = __class__.__name__
        temp_dict["created_at"] = self.created_at.isoformat()
        temp_dict["updated_at"] = self.updated_at.isoformat()
        return temp_dict

    def __str__(self):
        """Prints [<class name>] (<self.id>) <self.__dict__>"""
        c_name = __class__.__name__
        return "[{}] ({}) {}".format(c_name, self.id, self.__dict__)
