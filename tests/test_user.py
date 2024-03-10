#!/usr/bin/python3
"""
This module define tests for the User class
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test cases for the User class
    """

    def setUp(self):
        """
        Set up a new instance of the User class for each test case.
        """
        self.user = User()

    def test_init(self):
        """
        Test the initialization of a new User instance
        """
        self.assertIsInstance(self.user.email, str)
        self.assertEqual(self.user.email, "")
        self.assertIsInstance(self.user.password, str)
        self.assertEqual(self.user.password, "")
        self.assertIsInstance(self.user.first_name, str)
        self.assertEqual(self.user.first_name, "")
        self.assertIsInstance(self.user.last_name, str)
        self.assertEqual(self.user.last_name, "")

    def test_str(self):
        """
        Test the string representation of a User instance
        """
        expected_str = f"[User] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(str(self.user), expected_str)


if __name__ == "__main__":
    unittest.main()
