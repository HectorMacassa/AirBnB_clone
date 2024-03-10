#!/usr/bin/python3
"""
This module defines tests forFileStorage class
"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test cases for FileStorage class
    """

    def setUp(self):
        """
        Set up a new  instance of the FileStorage class for each test case
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        Remove the JSON file after each test case
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """
        Test the all  method of the FileStorage class
        """
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """
        Test the new method of the FileStorage class
        """
        model = BaseModel()
        self.storage.new(model)
        key = f"{model.__class__.__name__}.{model.id}"
        self.assertIn(key, self.storage.all().keys())

    def test_save(self):
        """
        Test the save method of the FileStorage class
        """
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """
        Test reload method of the FileStorage class
        """
        model = BaseModel()
        user = User()
        self.storage.new(model)
        self.storage.new(user)
        self.storage.save()
        self.storage.reload()
        key = f"{model.__class__.__name__}.{model.id}"
        key = f"{user.__class__.__name__}.{user.id}"
        self.assertIn(key_model, self.storage.all().keys())
        self.assertIn(key_user, self.storage.all().keys())


if __name__ == "__main__":
    unittest.main()
