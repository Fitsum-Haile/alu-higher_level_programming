#!/usr/bin/python3
"""Defines a class Square."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (float or int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Define equality comparison based on square area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define inequality comparison based on square area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define less than comparison based on square area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define less than or equal to comparison based on square area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define greater than comparison based on square area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define greater than or equal to comparison based on square area."""
        return self.area() >= other.area()
