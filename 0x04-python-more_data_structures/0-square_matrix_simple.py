#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [list(map(lambda n: n ** 2, row)) for row in matrix]
    return (new)
