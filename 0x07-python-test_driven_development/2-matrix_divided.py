#!/usr/bin/python3
"""Write a function all elements of a matrix."""


def matrix_divided(matrix, div):
    """Return a new matrix.
    

    Args:
        matrix (list): list of lists.
        div (int/float): divisor
    Raises:
        TypeError: if matrix is not list of lists containing integers or floats
        TypeError: if the rows in matrix are of different size
        TypeError: if div is not an integer or float
        ZeroDivisionError: if div is equal to zero
    Return:
        A new matrix consisting according to rows of elements of the matrix divided by div
    """
    if (not isinstance(matrix, list) or 
            not all(isinstance(i, list) for i in matrix) or
            not all(isinstance(j, (int, float))
                    for j in [num for i in matrix for num in i])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix): 
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number") 

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
