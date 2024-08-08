#!/usr/bin/python3
"""Module for the add_integer function."""


def add_integer(a, b=98):
    """Add two integers or floats."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
