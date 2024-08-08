#!/usr/bin/python3

"""
This module contains a function that divides all elements of a matrix
by a number and rounds to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number and rounds to 2
    decimal places.
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
