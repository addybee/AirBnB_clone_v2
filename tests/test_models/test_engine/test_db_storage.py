#!/usr/bin/python3
""" Module for testing db storage"""


import unittest
# from models.base_model import BaseModel, Base
from models import storage
from models.state import State
from os import getenv


class test_dbStorage(unittest.TestCase):
    """ Class to test the file storage method """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        def setUp(self):
            """ Set up test environment """
            del_list = []
            for val in storage.all().values():
                del_list.append(val)
            for obj in del_list:
                storage.delete(obj)

        def tearDown(self):
            """ Remove storage file at end of tests """
            pass

        def test_obj_list_empty(self):
            """ __objects is initially empty """
            self.assertEqual(len(storage.all()), 0)

        def test_new(self):
            """ New object is correctly added to __objects """
            new = State()
            storage.new(new)
            for obj in storage.all().values():
                temp = obj
                self.assertTrue(temp is obj)

        def test_all(self):
            """ __objects is properly returned """
            new = State(name="rolland")
            storage.new(new)
            storage.save()
            temp = storage.all()
            lent = len(temp.keys())
            self.assertIsInstance(temp, dict)
            self.assertGreater(lent, 0)

        # def test_base_model_instantiation(self):
        #     """ File is not created on BaseModel save """
        #     new = BaseModel()
        #     self.assertFalse(os.path.exists('file.json'))

        def test_empty_save(self):
            """ Data is saved to DB """
            lent = len(storage.all(State).keys())
            new = State()
            storage.new(new)
            # storage.save()
            lent1 = len(storage.all(State).keys())
            self.assertEqual(lent, lent1)
