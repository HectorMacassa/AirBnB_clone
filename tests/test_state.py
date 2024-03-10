#!/usr/bin/python3
"""
This module defines Test cases for the STate class
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """

    def setUp(self):
        """
        Set up a new instance of the State class for each test case.
        """
        self.state = State()

    def test_init(self):
        """
        Test the initialization of a new State instance.
        """
        self.assertIsInstance(self.state.name, str)
        self.assertEqual(self.state.name, "")

    def test_str(self):
        """
        Test the string representation of a State instance.
        """
        expected_str = f"[State] ({self.state.id}) {self.state.__dict__}"
        self.assertEqual(str(self.state), expected_str)


if __name__ == "__main__":
    unittest.main()
