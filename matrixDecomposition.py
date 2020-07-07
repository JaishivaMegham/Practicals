import numpy as np

matrix_1_lst = [ [2,0,3],
                 [3,1,3],
                 [4,-1,1]
                ]

eign_details = np.linalg.eig(matrix_1_lst)
print ( "Eigen value for this matrix is  {}".format(eign_details[0]))
print('')
print('')
print ( "Eigen vector for this matrix P is  {}".format(eign_details[1]))
print('')
print('')

eigen_vector_inverse = np.linalg.inv(eign_details[1])
eigen_value_diagonal = np.diag(eign_details[0])

print ( "Eigen vector for Inverse matrix P^-1 is  {}".format(eigen_vector_inverse))
print('')
print('')
print ( "Eigen Value's Diagonal matrix D is  {}".format(eigen_value_diagonal))
print('')
print('')

final_matrix_A = np.dot(eign_details[1],np.dot(eigen_value_diagonal,eigen_vector_inverse))
print ( "final Matrix A  after Eigen decompostion and diagonalization is {}" .format(final_matrix_A))

print(np.allclose(np.dot(final_matrix_A, np.array(matrix_1_lst)), np.eye(np.array(matrix_1_lst).shape[0])))