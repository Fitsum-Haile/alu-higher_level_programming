#!/usr/bin/python3
"""
Module to add all command-line arguments to a Python list
and save them to a file in JSON format.
"""

import sys
from os.path import exists
from importlib import import_module

# Import functions from previous tasks
save_to_json_file = import_module('5-save_to_json_file').save_to_json_file
load_from_json_file = import_module('6-load_from_json_file').load_from_json_file

def main():
    """
    Main function to handle adding command-line arguments to a list
    and saving them to a JSON file.
    """
    filename = "add_item.json"

    # Check if the file exists
    if exists(filename):
        # Load existing data from the file
        ite

