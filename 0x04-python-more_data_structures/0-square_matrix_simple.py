#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in matrix:
        new_matrix.append(list(map(lambda x: x**2, x)))
    return (new_matrix)
    
    """
    for x in ([x**2 for x in row] for row in matrix):
        new_matrix.append(x)
    return new_matrix
    """
