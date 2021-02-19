import scipy.linalg as la 
import numpy as np

# 1. Scipy Linear Algebra
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

# 2. Scipy Statistics
from scipy import stats
import matplotlib.pyplot as plt
# a. Create a discrete random variable with poissonian distribution and plot its probability mass function (PMF), 
# cummulative distribution function (CDF) and a histogram of 1000 random realizations of the variable
X = stats.poisson(3.5)
n = np.arange(0, 15)
fig, axes = plt.subplots(3,1, sharex=True)
# plot the probability mass function (PMF)
axes[0].step(n, X.pmf(n))
# plot the commulative distribution function (CDF)
axes[1].step(n, X.cdf(n))
# plot histogram of 1000 random realizations of the stochastic variable X
axes[2].hist(X.rvs(size=1000))
# plt.show()

# b. Create a continious random variable with normal distribution and plot its probability mass function (PMF), 
# cummulative distribution function (CDF) and a histogram of 1000 random realizations of the variable
Y = stats.norm()
x = np.linspace(-5,5,100)
fig, axes = plt.subplots(3,1, sharex=True)
# plot the probability distribution function (PDF)
axes[0].plot(x, Y.pdf(x))
# plot the commulative distributin function (CDF)
axes[1].plot(x, Y.cdf(x))
# plot histogram of 1000 random realizations of the stochastic variable Y
axes[2].hist(Y.rvs(size=1000), bins=50)
# plt.show()

# c. Test if two sets of (independent) random data comes from the same distribution
t_statistic, p_value = stats.ttest_ind(X.rvs(size=1000), X.rvs(size=1000))
print ("t-statistic =", t_statistic)
print ("p-value =", p_value)
t_statistic, p_value = stats.ttest_ind(Y.rvs(size=1000), Y.rvs(size=1000))
print ("t-statistic =", t_statistic)
print ("p-value =", p_value)