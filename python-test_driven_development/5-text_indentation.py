#!/usr/bin/python3
"""
Module for text indentation.
"""

def text_indentation(text):
    """
    Function that formats a string with proper indentation.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = ['.', '?', ':']
    new_text = ""
    indent = False

    for char in text:
        if char in punctuation_marks:
            new_text += char
            new_text += '\n\n'
            indent = True
        else:
            if indent and char == ' ':
                continue
            else:
                new_text += char
                indent = False

    # Print the result, ensuring proper formatting
    result = '\n'.join(line.strip() for line in new_text.strip().split('\n'))
    print(result)
