#!/usr/bin/python3
"""

A module that representes the class FileStorage

"""

from json import dumps, loads
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    A class FileStorage that serializes instances to a
    JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            self.__objects["{}.{}".format(
                obj.__class__.__name__, obj.id)] = obj

    def save(self):
        new_dict = {}
        for k, v in self.__objects.items():
            new_dict[k] = v.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as my_file:
            my_file.write(dumps(new_dict))

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as my_file:
                obj = loads(my_file.read())
            for k, v in obj.items():
                class_name = k.split('.')[0]
                self.__objects[k] = eval(class_name)(**v)
        except BaseException:
            pass
