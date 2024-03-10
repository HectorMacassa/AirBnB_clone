#!/usr/bin/python3
"""
This module deines test for the City class
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    def setUp(self):
        """
        Set up a new instance of the City class for each test case.
        """
        self.city = City()

    def test_init(self):
        """
        Test the initialization of a new City instance.
        """
        self.assertIsInstance(self.city.state_id, str)
        self.assertEqual(self.city.state_id, "")
        self.assertIsInstance(self.city.name, str)
        self.assertEqual(self.city.name, "")

    def test_str(self):
        """
        Test the string representation of a City instance.
        """
        expected_str = f"[City] ({self.city.id}) {self.city.__dict__}"
        self.assertEqual(str(self.city), expected_str)


if __name__ == "__main__":
    unittest.main()
