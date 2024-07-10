#!/usr/bin/python3
'''
A class Rectangle defined by width and height attribute
'''


class Rectangle:
    '''
    Represents a rectangle with private instance attributes
    '''
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

    @property
    def width(self):
        '''
        Gets the width of the rectangle
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Sets the width of the rectangle
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        '''
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''
        Gets the height of the rectangle
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Sets the height of the rectangle
        Raises:
            TypeError: if height is not an integer
            valueError: if height is less than 0
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

