#!/usr/bin/python3
"""
This module defines tests for base_mode.py
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """
        Set up a new instance of the BaseModel class for each test case.
        """
        self.model = BaseModel()

    def test_init(self):
        """
        Test the initialization of a new BaseModel instance.
        """
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertNotEqual(self.model.created_at, self.model.updated_at)

    def test_str(self):
        """
        Test the string representation of a BaseModel instance.
        """
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)

    def test_save(self):
        """
        Test the save method of a BaseModel instance.
        """
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """
        Tests the to_dict method of a BaseModel instance.
        """
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn("__class__", model_dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertIn("created_at", model_dict)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIn("updated_at", model_dict)
        self.assertIsInstance(model_dict["updated_at"], str)

if __name__ == "__main__":
    unittest.main()
