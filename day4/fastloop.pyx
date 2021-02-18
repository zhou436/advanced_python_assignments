cimport numpy as np
import math

def rbf_network_cython(np.ndarray[np.float64_t, ndim=2] X, np.ndarray[np.float64_t, ndim=1] beta, int theta):
    cdef int N, D, i, j, d
    cdef float Y[1000]
    cdef float r
    
    N = X.shape[0]
    D = X.shape[1]

    for i in range(N):
        for j in range(N):
            r = 0
            for d in range(D):
                r += (X[j, d] - X[i, d]) ** 2
            r = r**0.5
            Y[i] += beta[j] * math.exp(-(r * theta)**2)

    return Y