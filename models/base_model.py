#!/usr/bin/python3
"""

A module that representes a BaseModel class

"""


import uuid
from datetime import datetime

class BaseModel:
    """
    A class BaseModel that defines all common
    attributes/methods for other classes
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.id} {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        self.__dict__.update({'__class__': self.__class__.__name__})
        return self.__dict__



