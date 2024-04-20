#!/usr/bin/python3
""" define the test for place class """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ test Place"""

    def __init__(self, *args, **kwargs):
        """ constructor """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ test city id """
        new = self.value(city_id="2")
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ test user id """
        new = self.value(user_id="12")
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ test name """
        new = self.value(name="maldives")
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ test descriptor """
        new = self.value(description="i am jean and i love the house")
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ test number of rooms """
        new = self.value(number_rooms=5)
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ test number of bathrooms """
        new = self.value(number_bathrooms=5)
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ test maximum number of guest """
        new = self.value(max_guest=3)
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ test price by night """
        new = self.value(price_by_night=876)
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ test latitude """
        new = self.value(latitude=34.213)
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ test longitude """
        new = self.value(longitude=92.234)
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """ test amenity id """
        new = self.value(amenity_ids=[1, 2, 3])
        self.assertEqual(type(new.amenity_ids), list)
