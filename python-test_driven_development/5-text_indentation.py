#!/usr/bin/python3
"""
Prints a text with 2 new lines after each of these characters: ., ? and :.
"""

def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    characters = ".?:"
    new_text = ""
    for char in text:
        new_text += char
        if char in characters:
            new_text += "\n\n"
    
    # Remove trailing spaces on each line
    lines = new_text.split("\n")
    trimmed_lines = [line.strip() for line in lines]
    final_text = "\n".join(trimmed_lines)
    
    print(final_text)
