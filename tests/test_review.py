#!/usr/bin/python3
"""
This module defines test for the Review class
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """

    def setUp(self):
        """
        Set up a new instance of the Review class for each test case.
        """
        self.review = Review()

    def test_init(self):
        """
        Test the initialization of a new Review instance.
        """
        self.assertIsInstance(self.review.place_id, str)
        self.assertEqual(self.review.place_id, "")
        self.assertIsInstance(self.review.user_id, str)
        self.assertEqual(self.review.user_id, "")
        self.assertIsInstance(self.review.text, str)
        self.assertEqual(self.review.text, "")

    def test_str(self):
        """
        Test the string representation of a Review instance.
        """
        expected_str = f"[Review] ({self.review.id}) {self.review.__dict__}"
        self.assertEqual(str(self.review), expected_str)


if __name__ == "__main__":
    unittest.main()
