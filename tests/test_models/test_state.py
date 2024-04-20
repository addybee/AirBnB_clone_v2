#!/usr/bin/python3
""" define the test for state class """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ tst state """

    def __init__(self, *args, **kwargs):
        """ constructor """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ test the attribute type """
        new = self.value(name="Ogun")
        self.assertEqual(type(new.name), str)
