#!/usr/bin/python3
""" Module for testing db storage"""


import unittest
# from models.base_model import BaseModel, Base
from models import storage
from models.state import State


class test_dbStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for val in storage.all().values():
            del_list.append(val)
        for obj in del_list:
            storage.delete(obj)

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except Exception:
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
        new = State()
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
        storage.save()
        lent1 = len(storage.all(State).keys())
        self.assertNotEqual(lent, lent1)

    # def test_reload(self):
    #     """ Storage file is successfully loaded to __objects """
    #     new = BaseModel()
    #     storage.save()
    #     storage.reload()
    #     for obj in storage.all().values():
    #         loaded = obj
    #     self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    # def test_reload_empty(self):
    #     """ Load from an empty file """
    #     with open('file.json', 'w') as f:
    #         pass
    #     with self.assertRaises(ValueError):
    #         storage.reload()

    # def test_reload_from_nonexistent(self):
    #     """ Nothing happens if file does not exist """
    #     self.assertEqual(storage.reload(), None)

    # def test_base_model_save(self):
    #     """ BaseModel save method calls storage save """
    #     new = BaseModel()
    #     new.save()
    #     self.assertTrue(os.path.exists('file.json'))

    # def test_type_path(self):
    #     """ Confirm __file_path is string """
    #     self.assertEqual(type(storage._FileStorage__file_path), str)

    # def test_type_objects(self):
    #     """ Confirm __objects is a dict """
    #     self.assertEqual(type(storage.all()), dict)

    # def test_key_format(self):
    #     """ Key is properly formatted """
    #     new = BaseModel()
    #     _id = new.to_dict()['id']
    #     for key in storage.all().keys():
    #         temp = key
    #     self.assertEqual(temp, 'BaseModel' + '.' + _id)

    # def test_storage_var_created(self):
    #     """ FileStorage object storage created """
    #     from models.engine.file_storage import FileStorage
    #     print(type(storage))
    #     self.assertEqual(type(storage), FileStorage)

    # def test_delete(self):
    #     """ """
    #     new = BaseModel()
    #     obj_len = len(storage.all().keys())
    #     storage.delete(new)
    #     new_obj_len = len(storage.all().keys())
    #     self.assertTrue(obj_len > new_obj_len)

    # def test_delete_empty_param(self):
    #     """ """
    #     new = BaseModel()
    #     obj_len = len(storage.all().keys())
    #     storage.delete()
    #     new_obj_len = len(storage.all().keys())
    #     self.assertFalse(obj_len > new_obj_len)

    # def test_all_parameter(self):
    #     """ """
    #     new = BaseModel()
    #     new1 = State()
    #     temp = storage.all(BaseModel)
    #     self.assertIsInstance(temp, dict)
    #     for obj in temp.values():
    #         self.assertEqual(obj.to_dict()['__class__'], "BaseModel")

    #     for obj in storage.all(State).values():
    #         self.assertEqual(obj.to_dict()['__class__'], "State")
