#!/usr/bin/python3
"""This module contains a function that prints a
text with 2 new lines after each of these characters: ., ? and :.
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each
    of these characters: ., ? and :."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = [".", "?", ":"]
    result = ""
    for char in text:
        result += char
        if char in punctuation:
            result = result.rstrip() + "\n\n"
        elif char == " " and (result[-2:] == "\n\n" or not result):
            continue
        else:
            result += " "
    print(result.strip())
