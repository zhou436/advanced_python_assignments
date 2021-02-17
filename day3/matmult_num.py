# Program to multiply two matrices using nested loops
import random
import numpy as np

# @profile
def main():
    N = 250

    # NxN matrix
    X = np.random.randint(0, 100, [N, N])
    Y = np.random.randint(0, 100, [N, N])
    result = np.matmul(X, Y)
    print(result)

if main():
    main