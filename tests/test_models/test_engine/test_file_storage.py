#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
from models.state import State
from os import getenv, remove, path


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """
    if getenv("HBNB_TYPE_STORAGE") != "db":
        def setUp(self):
            """ Set up test environment """
            del_list = []
            for key in storage.all().keys():
                del_list.append(key)
            for key in del_list:
                storage.delete(storage.all()[key])

        def tearDown(self):
            """ Remove storage file at end of tests """
            try:
                remove('file.json')
            except Exception:
                pass

        def test_obj_list_empty(self):
            """ __objects is initially empty """
            self.assertEqual(len(storage.all()), 0)

        def test_new(self):
            """ New object is correctly added to __objects """
            new = BaseModel()
            for obj in storage.all().values():
                temp = obj
                self.assertTrue(temp is obj)

        def test_all(self):
            """ __objects is properly returned """
            new = BaseModel()
            temp = storage.all()
            self.assertIsInstance(temp, dict)

        def test_base_model_instantiation(self):
            """ File is not created on BaseModel save """
            new = BaseModel()
            self.assertFalse(path.exists('file.json'))

        def test_empty(self):
            """ Data is saved to file """
            new = BaseModel()
            thing = new.to_dict()
            new.save()
            new2 = BaseModel(**thing)
            self.assertNotEqual(path.getsize('file.json'), 0)

        def test_save(self):
            """ FileStorage save method """
            new = BaseModel()
            storage.save()
            self.assertTrue(path.exists('file.json'))

        def test_reload(self):
            """ Storage file is successfully loaded to __objects """
            new = BaseModel()
            storage.save()
            storage.reload()
            for obj in storage.all().values():
                loaded = obj
                self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

        def test_reload_empty(self):
            """ Load from an empty file """
            with open('file.json', 'w') as f:
                pass
            with self.assertRaises(ValueError):
                storage.reload()

        def test_reload_from_nonexistent(self):
            """ Nothing happens if file does not exist """
            self.assertEqual(storage.reload(), None)

        def test_base_model_save(self):
            """ BaseModel save method calls storage save """
            new = BaseModel()
            new.save()
            self.assertTrue(path.exists('file.json'))

        def test_type_path(self):
            """ Confirm __file_path is string """
            self.assertEqual(type(storage._FileStorage__file_path), str)

        def test_type_objects(self):
            """ Confirm __objects is a dict """
            self.assertEqual(type(storage.all()), dict)

        def test_key_format(self):
            """ Key is properly formatted """
            new = BaseModel()
            _id = new.to_dict()['id']
            for key in storage.all().keys():
                temp = key
                self.assertEqual(temp, 'BaseModel' + '.' + _id)

        def test_storage_var_created(self):
            """ FileStorage object storage created """
            from models.engine.file_storage import FileStorage
            self.assertEqual(type(storage), FileStorage)

        def test_delete(self):
            """ deletion from file storage"""
            new = BaseModel()
            storage.new(new)
            obj_len = len(storage.all().keys())
            storage.delete(new)
            new_obj_len = len(storage.all().keys())
            self.assertTrue(obj_len > new_obj_len)

        def test_delete_empty_param(self):
            """ deletion from file storage without param"""
            new = BaseModel()
            obj_len = len(storage.all().keys())
            storage.delete()
            new_obj_len = len(storage.all().keys())
            self.assertFalse(obj_len > new_obj_len)

        def test_all_parameter(self):
            """ test all method with param """
            new = BaseModel()
            new1 = State()
            temp = storage.all(BaseModel)
            self.assertIsInstance(temp, dict)
            for obj in temp.values():
                self.assertEqual(obj.to_dict()['__class__'], "BaseModel")

            for obj in storage.all(State).values():
                self.assertEqual(obj.to_dict()['__class__'], "State")
