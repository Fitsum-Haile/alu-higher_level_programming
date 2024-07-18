#!/usr/bin/python3
"""
Module: 7-add_item
"""

import sys
import os.path

def load_from_json_file(filename):
    """
    Load JSON data from a file.

    Args:
        filename (str): The name of the file to load from.

    Returns:
        list: The JSON-decoded data.
        If the file doesn't exist, returns an empty list.
    """
    if not os.path.exists(filename):
        return []

    with open(filename, mode='r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []
    return data

def save_to_json_file(my_obj, filename):
    """
    Save JSON data to a file.

    Args:
        my_obj (object): The Python object to save as JSON.
        filename (str): The name of the file to save to.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)

if __name__ == "__main__":
    import json

    filename = "add_item.json"
    my_list = load_from_json_file(filename)

    for arg in sys.argv[1:]:
        my_list.append(arg)

    save_to_json_file(my_list, filename)

