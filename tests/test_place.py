#!/usr/bin/pyhton3
"""
This module defines tests for Place class
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """

    def setUp(self):
        """
        Set up a new instance of the Place class for each test case.
        """
        self.place = Place()

    def test_init(self):
        """
        Test the initialization of a new Place instance.
        """
        self.assertIsInstance(self.place.city_id, str)
        self.assertEqual(self.place.city_id, "")
        self.assertIsInstance(self.place.user_id, str)
        self.assertEqual(self.place.user_id, "")
        self.assertIsInstance(self.place.name, str)
        self.assertEqual(self.place.name, "")
        self.assertIsInstance(self.place.description, str)
        self.assertEqual(self.place.description, "")
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertEqual(self.place.number_rooms, 0)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertEqual(self.place.max_guest, 0)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertIsInstance(self.place.latitude, float)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertIsInstance(self.place.longitude, float)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertIsInstance(self.place.amenity_ids, list)
        self.assertEqual(self.place.amenity_ids, [])

    def test_str(self):
        """
        Test the string representation of a Place instance.
        """
        expected_str = f"[Place] ({self.place.id}) {self.place.__dict__}"
        self.assertEqual(str(self.place), expected_str)


if __name__ == "__main__":
    unittest.main()
