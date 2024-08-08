#!/usr/bin/python3
"""Unittest for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_max_at_end(self):
        """Test with the maximum value at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test with the maximum value at the beginning of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test with the maximum value in the middle of the list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_one_negative_number(self):
        """Test with a list containing one negative number."""
        self.assertEqual(max_integer([-1, 0, 1, 2]), 2)

    def test_only_negative_numbers(self):
        """Test with a list of only negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_list_of_one_element(self):
        """Test with a list containing a single element."""
        self.assertEqual(max_integer([10]), 10)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_non_integers(self):
        """Test with a list of non-integer types.
        Note: The current function does not raise TypeError,
        so we check if the function runs without raising an exception.
        """
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')
        self.assertEqual(max_integer(['abc', 'def', 'ghi']), 'ghi')
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)

if __name__ == '__main__':
    unittest.main()
