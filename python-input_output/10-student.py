#!/usr/bin/python3
"""
Module: 10-student
"""


class Student:
    """
    Class representing a Student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        Args:
            attrs (list of str, optional): List of attribute names to retrieve.
                                           Defaults to None.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        elif isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        else:
            return self.__dict__
