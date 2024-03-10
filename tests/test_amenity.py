#!/usr/bin/python3
"""
This module defines test for the Amenity class
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def setUp(self):
        """
        Set up a new instance of the Amenity class for each test case.
        """
        self.amenity = Amenity()

    def test_init(self):
        """
        Test the initialization of a new Amenity instance.
        """
        self.assertIsInstance(self.amenity.name, str)
        self.assertEqual(self.amenity.name, "")

    def test_str(self):
        """
        Test the string representation of an Amenity instance.
        """
        expected_str = f"[Amenity] ({self.amenity.id}) {self.amenity.__dict__}"
        self.assertEqual(str(self.amenity), expected_str)


if __name__ == "__main__":
    unittest.main()
