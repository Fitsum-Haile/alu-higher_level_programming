#!/usr/bin/python3
import numpy as np

'''
 this module contains a function that multiplies 2 matrices
'''


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices
    Args:
        m_a (list): matrix a
        m_b (list): matrix b
    Returns:
        list: new matrix
    """
    return np.matmul(m_a, m_b)
