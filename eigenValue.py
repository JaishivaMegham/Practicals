# Load library
import numpy as np

matrixA =    np.array([[3, 0, 0],
                       [0, 3, 0],
                       [0, 0, 5]])

matrixB = np.array([[1,0],[0,1]])

eigenPair = np.linalg.eig(matrixA)

print('Eigen Value Pair: '+str(eigenPair))

eigenVal = eigenPair[0]

print('')
print('')

print('Eigen Value:' +str(eigenVal))

eigenVector = eigenPair[1]

print('')
print('')

print('Eigen Value:' +str(eigenVector))
print('')
print('')
print('Alternate way of finding only Eigen values is using: np.linalg.eigvals(matrixA) ')

print(np.linalg.eigvals(matrixA))
