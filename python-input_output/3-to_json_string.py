#!/usr/bin/python3
import json 
"""
Module to return the JSON representation of an object (string).
"""


def to_json_string(my_obj):
    """Return the JSON representation of an object (string).

    Args:
        my_obj (any): The object to convert to JSON string.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
