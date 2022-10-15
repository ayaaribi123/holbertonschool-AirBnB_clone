#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel

class Test_Class_BaseModel(unittest.TestCase):
    def test_class_type(self):
        A = BaseModel()

        self.assertTrue(A, '<class base_model.BaseModel>')

    def test_is_instance(self):
        B = BaseModel()

        self.assertIsInstance(B, BaseModel)

    def test_adding_attributes(self):
        a = BaseModel()
        a.name = "mYmODEL"
        a.number = 90

        self.assertTrue(hasattr(a, 'name'))
        self.assertEqual(a.name, 'mYmODEL')
        self.assertEqual(a.number, 90)

    def test_attributes(self):
        C = BaseModel()

        self.assertTrue(type(C.id), '<class str>')
        self.assertTrue(type(C.created_at), '<class datetime.datetime>')
        self.assertTrue(type(C.updated_at), '<class datetime.datetime>')

    def testFunction_str(self):
        D = BaseModel()
        myStr = str(D)


        self.assertEqual(myStr, f"[{D.__class__.__name__}] ({D.id}) {D.__dict__}")

    def testFunction_save(self):
        b = BaseModel()
        before_save = b.updated_at
        b.save()
        after_save = b.updated_at

        self.assertEqual(b.updated_at.replace(microsecond=0), datetime.now().replace(microsecond=0))
        self.assertNotEqual(before_save, after_save)

    def testFunction_to_dict(self):
        c = BaseModel()
        c_json = c.to_dict()

        self.assertIn('__class__', c_json)
        self.assertTrue(type(c.created_at), '<class str>')
        self.assertTrue(type(c.updated_at), '<class str>')
