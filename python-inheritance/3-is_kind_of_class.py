#!/usr/bin/python3
"""Defines a function is_kind_of_class."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of,
    or if obj is an instance of a class
    that inherited from, the specified class; otherwise False.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a_class or its subclass,
        else False.
    """
    return isinstance(obj, a_class)
