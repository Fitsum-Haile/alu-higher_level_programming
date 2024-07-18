#!/usr/bin/python3

"""
Module: 100-append_after

Contains a function to append text after each line containing a specific string in a file.
"""


def append_after(filename="", textsearch="", textappend=""):
    """
    Append a line of text after each line containing a specific string in a file.

    Args:
        filename (str): The name of the file to modify.
        textsearch (str): The string to search for in each line.
        textappend (str): The text to append after each found line.
    """
    try:
        with open(filename, 'r+') as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                f.write(line)
                if textsearch in line:
                    f.write(textappend)
    except FileNotFoundError:
        pass  # Handle the case where the file doesn't exist gracefully

# Example usage
if __name__ == "__main__":
    append_after("file_not", "c", "Python is cool!\n")
