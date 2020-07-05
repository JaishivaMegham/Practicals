# Load library
import numpy as np
from numpy.linalg import inv

# Return matrix rank
def matrixInverse(matrixinput):
    matinv = inv(matrixinput)
    return matinv

# Create matrix
matrixA = np.array([[1,2],[3,4]])

print('Given Matrix is: ')
print(matrixA)
print('')

matInverse = matrixInverse(matrixA)

print('Inverse Matrix is: ')
print(matInverse)
print('')

print('Validation')
print('Multiplying the Input Matrix with its Inverse to check for Identity')
dot_mat_matinv = np.dot(matrixA,matInverse)
print(dot_mat_matinv)

#Comparing the dot product of matrix and its inverse with digonal matrix of 1

print(np.allclose(np.dot(matrixA, matInverse), np.eye(matrixA.shape[0])))
