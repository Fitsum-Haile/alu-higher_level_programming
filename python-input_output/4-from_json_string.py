#!/usr/bin/python3
import json
"""
Module to convert JSON string to Python object.
"""


def from_json_string(my_str):
    """Converts a JSON string to a Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)

