#!/usr/bin/python3


import math

class MagicClass:
    """
    Represents a magic class for calculating properties of a circle.

    Attributes:
        __radius (float): The radius of the circle.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance with a given radius.

        Args:
            radius (float): The radius of the circle. Defaults to 0.

        Raises:
            TypeError: If radius is not a number (int or float).
        """
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
