#!/usr/bin/python3

def matrix_divided(matrix, div):
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, int) or isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix[1:]):
        raise TypeError("Each row of the matrix must have the same size")

    result = []
    for row in matrix:
        new_row = []
        for i in row:
            if not isinstance(i, int) or not isinstance(i, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(i / div, 2))
        result.append(new_row)
    return result
