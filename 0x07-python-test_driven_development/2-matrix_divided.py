#!/usr/bin/python3
"""
Defines a matrix division function.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a specified divisor.

    Parameters:

    matrix (list of lists): The input matrix, containing integers or floats.
    div (number): The divisor, which must be a non-zero integer or float.
    Returns:

    A new matrix where all elements have been divided by div,
    rounded to two decimal places.
    Raises:

    TypeError if the input matrix is not a list of lists of integers/floats,
    if the rows have different sizes, or if div is not a number.
    ZeroDivisionError if div is equal to 0.
    """
    if not isinstance(matrix, list) or len(matrix) == 0 or \
            not all(isinstance(row, list) or row == [] for row in matrix) or \
            not all(isinstance(x, (int, float))for row in matrix for x in row):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round((x / div), 2) for x in row] for row in matrix]
