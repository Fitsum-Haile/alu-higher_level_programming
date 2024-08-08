#!/usr/bin/python3
"""This module contains a function that prints a text with 2 new lines after each of these characters: ., ? and :."""


def text_indentation(text):
    """Prints a text with 2 new lines after each
    of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(0, len(text)):
        print(text[i], end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print("\n")
            if i < len(text) - 1 and text[i + 1] == " ":
                i += 1
