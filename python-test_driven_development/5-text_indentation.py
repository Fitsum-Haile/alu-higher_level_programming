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
    previous_char = None
    for char in text:
        if char in punctuation:
            result += char + "\n\n"
        else:
            if previous_char in punctuation:
                result = result.rstrip() + " "
            result += char
        previous_char = char
    print(result.strip())
