#!/usr/bin/python3
from models.base_model import BaseModel


class State(BaseModel):
    """State class that iherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor for State class"""
        super().__init__(*args, **kwargs)
