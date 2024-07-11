#!/usr/bin/python3
"""
A class Rectangle defined by width and height attributes
"""


class Rectangle:
    """
    Represents a rectangle with private instance attributes
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        If width or height is equal to 0, perimeter is equal to 0
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
