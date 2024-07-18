#!/usr/bin/python3

"""
Module to load Python object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """Loads a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        any: The Python object loaded from the JSON file.
    """
    with open(filename, 'r') as f:
        return json.load(f)
