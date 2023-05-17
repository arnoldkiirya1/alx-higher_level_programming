#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    
    # Iterate over the elements of the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Compute the square of each element and store it in the corresponding position of the result matrix
            result[i][j] = matrix[i][j] ** 2
    
    # Return the resulting matrix
    return result
