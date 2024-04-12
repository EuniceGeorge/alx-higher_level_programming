#!/usr/bin/python3
"""
This module divides all elements of a matrix by an integer

The matrix must be a list of lists of integers/floats
Each row of the matrix must be thesame size

else it raises an error
"""


def matrix_divided(matrix, div):

    """
    It returns the result of the divivded matrix
    """


    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix[1:]):
        """
        scan through all the row excluding the first row
        """
        raise TypeError("Each row of the matrix must have the same size")

    result = []
    for row in matrix:
        new_row = []
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(i / div, 2))
        result.append(new_row)
    return result
