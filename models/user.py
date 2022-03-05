#!/usr/bin/python3
"""User class module"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User class that inherits from BaseModel
        to use its id, created_at and updated_at attributes
    """
    """Class attributes for User class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
