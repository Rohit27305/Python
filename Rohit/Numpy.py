import numpy as np

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Addition 
result_addition = np.add(matrix1, matrix2)
print("Addition of two matrices:")
print(result_addition)

# Transpose 
transpose_matrix1 = np.transpose(matrix1)
transpose_matrix2 = np.transpose(matrix2)
print("Transpose of matrix 1:")
print(transpose_matrix1)
print("Transpose of matrix 2:")
print(transpose_matrix2)
