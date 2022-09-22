#!/usr/bin/python3
"""
Module Devide Matrix
"""


def matrix_divided(matrix, div):
    """
    Devides all elements in matrix
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(matrix) is not list or not all((type(le) is list)for le in matrix)\
        or not all((isinstance(n, (int, float))for n in le)for le in matrix)\
            or len(matrix[0]) == 0:
        raise TypeError(
                "matrix must be a matrix "
                "(list of lists) of integers/floats")
    le = len(matrix[0])
    if not all((len(x) == le)for x in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return [list(map(lambda x: round(x / div, 2), r))for r in matrix]
