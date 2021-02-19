import scipy.linalg as la 
import numpy as np


# a. Define a matrix A
# b. Define a vector b
# c. Solve the linear system of equations A x = b
# d. Check that your solution is correct by plugging it into the equation
A = np.array([[3,2,0],[1,-1,0],[0,5,1]])
b = np.array([2,4,-1])

x = la.solve(A, b)
print(np.dot(A, x) == b)

# e. Repeat steps a-d using a random 3x3 matrix B (instead of the vector b)
B = np.random.rand(3,3)

X = la.solve(A, B)
print(np.dot(A, X) == B)

# f. Solve the eigenvalue problem for the matrix A and print the eigenvalues and eigenvectors
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
Eig_A = la.eigh(A)
print(Eig_A)

# g. Calculate the inverse, determinant of A
print(la.inv(A))
print(la.det(A))

# h. Calculate the norm of A with different orders
print("Order 1: {}".format(la.norm(A, ord = 1)))
print("Order 2: {}".format(la.norm(A, ord = 2)))