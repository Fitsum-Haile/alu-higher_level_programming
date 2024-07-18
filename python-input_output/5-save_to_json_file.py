#!/usr/bin/python3

"""
Module to save Python object to a JSON file.
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes a Python object to a JSON file.

    Args:
        my_obj (any): The object to serialize to JSON and save.
        filename (str): The name of the file to save the JSON data.

    Returns:
        None
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
