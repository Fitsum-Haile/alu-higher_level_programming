#!/usr/bin/python3
"""This module contains a function that prints a text with 2 new lines after each of these characters: ., ? and :."""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = [".", "?", ":"]
    result = ""
    for char in text:
        if char in punctuation:
            result = result.rstrip() + char + "\n\n"
        elif char == " " and (result.endswith("\n\n") or not result):
            continue
        else:
            result += char
    print(result.strip())
