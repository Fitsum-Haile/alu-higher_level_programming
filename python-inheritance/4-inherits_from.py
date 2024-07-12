#!/usr/bin/python3
"""Defines a function inherits_from."""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class, else False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
