#!/usr/bin/python3
"""Defines a function is_same_class."""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class, otherwise False.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        bool: True if obj is exactly an instance of a_class, else False.
    """
    return type(obj) is a_class
