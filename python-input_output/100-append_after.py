#!/usr/bin/python3
"""
Module: 100-append_after

This module provides a function to insert a line of text into a file after each
line containing a specific string.

Functions:
- append_after(filename="", textsearch="", textappend=""): Inserts textappend
  after each occurrence of textsearch in the file specified by filename.

"""


def append_after(filename="", textsearch="", textappend=""):
    """
    Inserts a line of text after each line containing a specific string in a file.

    Args:
        filename (str): The name of the file to modify.
        textsearch (str): The string to search for in each line.
        textappend (str): The line of text to insert after each found line.

    Notes:
        - This function modifies the file directly. If the file does not exist,
          it silently returns without performing any modifications.
        - Uses the with statement for file handling, ensuring files are properly
          closed after operations.

    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        return

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if textsearch in line:
                file.write(textappend)

if __name__ == "__main__":
    # Test cases as per the requirements
    append_after("file1.txt", "c", "Python is cool!\n")
    append_after("file2.txt", "c", "Python is cool!\n")
    append_after("file3.txt", "c is fun", "Python is cool!\n")
    append_after("file4.txt", "c", "Python")
    append_after("non_existing_file.txt", "c", "Python")
