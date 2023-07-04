#!/usr/bin/python3
"""Function that divides all elements of the natrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix with matrix which is the
    lists of ints or float and div which is the divisor arg.
    Raise TypeError if matrix contains non-number, rows of
    different sizes and div not int or float. Raise
    ZeroDivisionError if div is 0.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
