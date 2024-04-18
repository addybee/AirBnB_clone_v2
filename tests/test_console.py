""" test suit fie console.py """
import sys
import models
import unittest
from io import StringIO
from console import HBNBCommand
from unittest.mock import create_autospec


class test_console(unittest.TestCase):
    """ Test the console module """
    def setUp(self):
        """setup for"""
        self.tempIO = sys.stdout
        self.outputIO = StringIO()
        sys.stdout = self.outputIO

    def tearDown(self):
        """ """
        sys.stdout = self.tempIO

    def instanceHBNB(self):
        """ create an instance of the HBNBCommand class """
        return HBNBCommand()

    def test_create(self):
        """Test that create works"""
        console = self.instanceHBNB()
        console.onecmd("create User name=\"poland\"")
        self.assertTrue(isinstance(self.outputIO.getvalue(), str))
        console.onecmd("create User name=\"po\\\"land\"")
        self.assertTrue(isinstance(self.outputIO.getvalue(), str))

    def test_create_missing_class(self):
        """ """
        console = self.instanceHBNB()
        console.onecmd("create")
        screen = self.outputIO.getvalue()
        self.assertEqual(screen, "** class name missing **\n")

    def test_create_invalid_class(self):
        """ """
        console = self.instanceHBNB()
        console.onecmd("create LGA name=\"OJO\"")
        screen = self.outputIO.getvalue()
        self.assertEqual(screen, "** class doesn't exist **\n")
