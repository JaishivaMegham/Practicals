import numpy

# Function to multiply two matrices using nested loops

def dotProduct(matrixA, matrixB):

    endProduct = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

    # iterate through rows of matrixA
    for i in range(len(matrixA)):

        # iterate through number of columns of matrixB.
        for j in range(len(matrixB[0])):

            # iterate through rows of matrixB
            for k in range(len(matrixB)):

                endProduct[i][j] += matrixA[i][k] * matrixB[k][j]

    for r in endProduct:
        print(r)
