#!/usr/bin/python3
"""Square class definition with size validation, area calculation,
printing capabilities, and position handling."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2
            positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character #.

        If size is 0, print an empty line.
        Use position to adjust the printing location.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
