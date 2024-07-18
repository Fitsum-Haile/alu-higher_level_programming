#!/usr/bin/python3
"""
Module: 8-class_to_json
"""


def class_to_json(obj):
    """
    Convert an instance of MyClass to a JSON serializable dictionary.

    Args:
        obj (object): An instance of MyClass.

    Returns:
        dict: A dictionary representation of the
        object suitable for JSON serialization.
    """
    attrs = obj.__dict__
    json_dict = {}

    for key, value in attrs.items():
        if not key.startswith('__') and \
                isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value

    return json_dict
