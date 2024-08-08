#!/usr/bin/python3
"""
Module base
Defines the Base class for managing the id attribute.
"""

class Base:
    """
    Base class for all future classes in the project.
    Manages the id attribute to avoid duplication of code and bugs.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new Base instance.

        Args:
            id (int, optional): The id of the instance. If None, it will be
                                automatically assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
