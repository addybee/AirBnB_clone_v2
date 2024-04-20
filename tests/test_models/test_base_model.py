#!/usr/bin/python3
""" define the test for Basemodel class """


from models import BaseModel, storage
import unittest
import datetime
from uuid import UUID
import json
from os import getenv


class test_basemodel(unittest.TestCase):
    """ test Basemodel """

    def __init__(self, *args, **kwargs):
        """ constructor """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ set up for each test in the Basemode """
        pass

    def tearDown(self):
        """clean up after each test in Basemodel """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """ test the instance of the class"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ test kwargs """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ test kwargs type"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        if getenv("HBNB_TYPE_STORAGE") != "db":
            i = self.value()
            i.save()
            key = self.name + "." + i.id
            with open('file.json', 'r') as f:
                j = json.load(f)
                self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ test the __str__ method of the class """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ test to dictionary method """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ test empty kwargs """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    @unittest.skip("the can no longer be catch")
    def test_kwargs_one(self):
        """ test kwargs for invalid key"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ test id """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ test created at"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ test updated at """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_kwargs_one_2(self):
        """ test kwargs for id, updated and created not
            present in the new obj dictionary
        """
        n = {'Name': 'test'}
        new = self.value(**n)
        new_dic = new.to_dict()
        self.assertEqual(type(new.created_at), datetime.datetime)
        self.assertEqual(type(new.updated_at), datetime.datetime)
        self.assertEqual(type(new.id), str)
        self.assertGreater(len(new_dic), len(n))

    def test_delete(self):
        """ """
        if getenv("HBNB_TYPE_STORAGE") != "db":
            new = self.value()
            new.save()
            new2 = self.value()
            new2.save()
            old = storage.all(self.value)
            new.delete()
            self.assertGreater(len(old), len(storage.all(self.value)))
