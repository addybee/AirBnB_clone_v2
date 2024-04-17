#!/usr/bin/python3
""" define the test for Review class """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ test Review"""

    def __init__(self, *args, **kwargs):
        """ constructor """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ test place id """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ test user id """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ test text id"""
        new = self.value()
        self.assertEqual(type(new.text), str)
