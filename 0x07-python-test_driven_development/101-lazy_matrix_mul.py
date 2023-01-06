#!/usr/bin/python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Returns the products of m_a and m_b
    multiplied using Numpy

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second  matrix.

    """

    return (np.matmul(m_a, m_b))
