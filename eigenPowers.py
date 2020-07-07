# Load library
import numpy as np
from numpy.linalg import inv
from numpy.linalg import matrix_power

# Return matrix power
def matrixPower(matrixinput,powValue):
    matPow = matrix_power(matrixinput,powValue)
    return matPow

matrixA = np.array([[2, 0, 1],
                       [1, 1, 2],
                       [-1, 0, -2]])

eigenVal , eigenVector  = np.linalg.eig(matrixA)

print('Eigen Value:' +str(eigenVal))
print('')

print('Eigen Vector Value:' +str(eigenVector))
print('')


eigenPower = np.dot(np.dot(eigenVector,matrixPower(np.diag(eigenVal),50)),inv(eigenVector))

print('Eigen Power to 50 is eigenVector*(diagonal of eigenValue^50)*inverse of eigenVector:'+str(eigenPower))
