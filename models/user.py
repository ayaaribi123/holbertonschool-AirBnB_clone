#!/usr/bin/python3
"""

A module that representes the class User

"""

from models.base_model import BaseModel


class User(BaseModel):
    """class User that is a subclass of BaseModel class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
