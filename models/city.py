#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """City class that iherits from BaseModel"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor for City class"""
        super().__init__(*args, **kwargs)
