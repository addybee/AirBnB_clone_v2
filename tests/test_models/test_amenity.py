#!/usr/bin/python3
""" define the test for amenity class """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ test Amenity"""

    def __init__(self, *args, **kwargs):
        """ constructor """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ test name """
        new = self.value(name="carlifonia")
        self.assertEqual(type(new.name), str)
