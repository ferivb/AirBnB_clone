#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that iherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor for Amenity class"""
        super().__init__(*args, **kwargs)
