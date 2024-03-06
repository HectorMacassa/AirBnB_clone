#!/usr/bin/python3
"""
This module defines tests for base_mode.py
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(untitest.TestCase):
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
