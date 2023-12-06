#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix to store squared values (deep copy)
    new_matrix = [row[:] for row in matrix]
    
    # Iterate through each row and column to square the values
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = matrix[i][j] ** 2  # Square the value
            
    return new_matrix
