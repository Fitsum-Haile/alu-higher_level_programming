#!/usr/bin/python3
"""Unittest for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_positive_integers(self):
        """Test with a list of positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        """Test with a list of negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        """Test with a list of both positive and negative integers."""
        self.assertEqual(max_integer([-1, 0, 1, 2, -2]), 2)

    def test_single_element(self):
        """Test with a single-element list."""
        self.assertEqual(max_integer([10]), 10)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_none_argument(self):
        """Test with None as an argument."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_integers(self):
        """Test with a list of non-integer types."""
        with self.assertRaises(TypeError):
            max_integer(['a', 'b', 'c'])
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'a', 4])

    def test_max_at_start(self):
        """Test with a list where max is the first element."""
        self.assertEqual(max_integer([9, 2, 3, 1]), 9)

    def test_max_at_end(self):
        """Test with a list where max is the last element."""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

if __name__ == '__main__':
    unittest.main()
