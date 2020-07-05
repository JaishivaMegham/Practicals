# Load library
import numpy as np
from numpy.linalg import matrix_rank

# Return matrix rank
def matrixRank(matrixinput):
    mr = matrix_rank(matrixinput)
    return mr

# Create matrix
matrixA = np.array([[2, 2, 1, 7],
                       [-1, 2, 0, 3],
                       [3, 2, 1, 8],
                       [4, 2, 0, 8]])

print('Given Matrix is: ')
print(matrixA)

matRank = matrixRank(matrixA)

print('Rank of the given matrix is: ' +str(matRank))

if len(matrixA) != matRank:
    print('The given matrix is a Singular matrix. This matrix does not have an Inverse Matrix.')
else:
    print('Its a full rank matrix. Non-Singular matrix. This matrix has an Inverse Matrix')