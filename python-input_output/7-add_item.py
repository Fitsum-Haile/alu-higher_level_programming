#!/usr/bin/python3
"""
Module: 1-write_file
"""

def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text content to write to the file.

    Returns:
        int: Number of characters written to the file.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        nb_characters = f.write(text)
    return nb_characters
