#!/usr/bin/python3
"""
Module: 11-student
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

        json_dict = {}
        for attr in attrs:
            if isinstance(attr, str) and hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)

        return json_dict

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance with those from a dictionary.

        Args:
            json (dict): Dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
