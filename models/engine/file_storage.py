#!/usr/bin/python3
"""

A module that representes the class FileStorage

"""

import json
import os


class FileStorage:
    """
    A class FileStorage that serializes instances to a
    JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

#    def __init__(self):
    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj})

    def save(self):
        with open(FileStorage.__file_path, mode="a", encoding="utf-8") as my_file:
            json.dump(FileStorage.__objects, my_file)

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding='utf-8') as my_file:
                FileStorage.__objects = json.load(my_file)
#            FileStorage.new(new_object)
#        return FileStorage.__objects
