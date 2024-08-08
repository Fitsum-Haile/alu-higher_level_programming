#!/usr/bin/python3
"""
Prints a text with 2 new lines after each '.', '?', and ':'.
"""

def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?', and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"
    print("\n".join(line.strip() for line in result.split("\n")))
