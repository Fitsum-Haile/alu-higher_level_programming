#!/usr/bin/python3
"""
Module: 12-pascal_triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
        n (int): Number of rows to generate.

    Returns:
        list of lists: Pascal's Triangle as a list of lists of integers.
                       Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
