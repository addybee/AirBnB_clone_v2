#!/usr/bin/python3
""" define the test for user class """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ test user """

    def __init__(self, *args, **kwargs):
        """ constructor """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ test first name"""
        new = self.value(first_name="mark")
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ test last name"""
        new = self.value(last_name="showman")
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ test email"""
        new = self.value(email="markshow@g.com")
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ test password """
        new = self.value(password="hbry8y43ywx83")
        self.assertEqual(type(new.password), str)
