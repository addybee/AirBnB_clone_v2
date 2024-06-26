#!/usr/bin/python3
""" define the test for city class """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from os import getenv


class test_City(test_basemodel):
    """ test City """

    def __init__(self, *args, **kwargs):
        """ constructor """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ test state id """
        new = self.value(state_id="34533")
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ test name """
        new = self.value(name="San_jose")
        self.assertEqual(type(new.name), str)
