#!/usr/bin/python3
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class Test_Class_FileStorage(unittest.TestCase):
    def test_class_attributes(self):
        a = FileStorage()

        self.assertTrue(hasattr(a, '__file_path'))
        self.assertTrue(hasattr(a, '__objects'))

    def test_Function_all(self):
        b = FileStorage()
        my_objects = b.all()

        self.assertTrue(type(my_objects), '<class dict>')

    def test_Function_new(self):
        c = FileStorage()
        c.new(obj)

        self.assertTrue(type(obj), '<class dict>')
        self.assertIn(obj, self.__objects.values())

    def test_Function_save(self):
        d = FileStorage()
        d.new(obj)
        d.save()

        self.assertEqual(d.__file_path, "file.json")
        self.assertIn(obj, d.__objects)

    def test_Function_reload(self):
        e = FileStorage()
        e.new(obj)
        e.save()
        e.reload()
        objects = e.all()

        self.assertIsNotNone(obj.id)
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", objects.keys())


