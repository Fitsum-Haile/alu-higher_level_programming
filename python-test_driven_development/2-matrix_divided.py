#!/usr/bin/python3

"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number and rounds to 2 decimal places."""
    if type(matrix) is not list or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError(
                "Each row of the matrix must have the same size")
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
    
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(item / div, 2) for item in row] for row in matrix]
