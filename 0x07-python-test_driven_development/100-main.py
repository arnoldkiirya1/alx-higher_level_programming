#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[1, 2], [3, 4]]
result = matrix_mul(matrix1, matrix2)
print(result)

matrix3 = [[1, 2]]
matrix4 = [[3, 4], [5, 6]]
result = matrix_mul(matrix3, matrix4)
print(result)
