import numpy as np

# 1.a. Create a null vector of size 10 but the fifth value which is 1
null_vector = np.zeros(10)
print(null_vector)
null_vector[4] = 1
print(null_vector)

# 1.b. Create a vector with values ranging from 10 to 49
linspace_b = np.linspace(10, 49, num=40)
print(linspace_b)

# 1.c. Reverse a vector (first element becomes last)
linspace_b_reverse = np.flip(linspace_b)
print(linspace_b_reverse)

# 1.d. Create a 3x3 matrix with values ranging from 0 to 8
matrix_d = np.arange(9).reshape(3,3)
print(matrix_d)

# 1.e. Find indices of non-zero elements from [1,2,0,0,4,0]
array_e = np.array([1,2,0,0,4,0])
array_e_nnullIndex = np.where(array_e != 0)
print(array_e_nnullIndex)

# 1.f. Create a random vector of size 30 and find the mean value
random_f_30 = np.random.rand((30))
random_f_30_mean = np.mean(random_f_30)
print(random_f_30_mean)

# 1.g. Create a 2d array with 1 on the border and 0 inside
matrix_dimension = 5
matrix_g = np.zeros([matrix_dimension, matrix_dimension])
matrix_g[0,:] = 1
matrix_g[-1,:] = 1
matrix_g[:,0] = 1
matrix_g[:,-1] = 1
print(matrix_g)

# 1.h. Create a 8x8 matrix and fill it with a checkerboard pattern
matrix_dimension = 8
matrix_g = np.zeros((matrix_dimension,matrix_dimension),dtype=int)
matrix_g[1::2,::2] = 1
matrix_g[::2,1::2] = 1
print(matrix_g)

# 1.i. Create a checkerboard 8x8 matrix using the tile function
matrix_unit = np.array([[0,1],[1,0]])
matrix_i = np.tile(matrix_unit, (4,4))
print(matrix_i)

# 1.j. Given a 1D array, negate all elements which are between 3 and 8, in place
array_j = np.arange(11)
array_j_index = (array_j >= 3) & (array_j <= 8)
array_j[array_j_index] *= -1
print(array_j)

# 1.k. Create a random vector of size 10 and sort it
array_k = np.random.rand(10)
array_k_sort = np.sort(array_k)
print(array_k_sort)

# 1.l. Consider two random array A anb B, check if they are equal
rand_A = np.random.randint(0,2,5)
rand_B = np.random.randint(0,2,5)
equal_com = rand_A == rand_B
equal_arr = np.equal(rand_A, rand_B)
print(equal_com)
print(equal_arr)

# 1.m. How to convert an integer (32 bits) array into a float (32 bits) in place?
array_m_int = np.arange(10, dtype=np.int32)
print(array_m_int.dtype)
array_m_float = array_m_int.astype(np.float32)
print(array_m_float.dtype)

# 1.n. How to get the diagonal of a dot product?
array_n_A = np.arange(9).reshape(3,3)
array_n_B = array_n_A + 1
array_n_C = np.dot(array_n_A,array_n_B)
diag_C = array_n_C.diagonal()
print(array_n_C)
print(diag_C)