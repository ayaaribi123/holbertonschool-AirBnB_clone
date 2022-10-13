#!/usr/bin/python3
"""

A module that representes a BaseModel class

"""


from datetime import datetime
import models
from uuid import uuid4


class BaseModel:
    """
    A class BaseModel that defines all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """*args, **kwargs arguments for
        the constructor of a BaseModel"""
        kwargc = len(kwargs)
        if kwargc > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
