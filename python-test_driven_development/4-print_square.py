#!/usr/bin/python3
"""This module contains a function that prints a square."""


def print_square(size):
    """Prints a square with the character '#'."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(int(size)):
        print("#" * int(size))
