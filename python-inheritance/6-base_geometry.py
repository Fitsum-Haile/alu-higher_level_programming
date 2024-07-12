#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Represents a base geometry class."""

    def area(self):
        """Raises an exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")
