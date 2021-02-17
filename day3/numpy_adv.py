import numpy as np

# a. Given a list of XYZ-coordinates, p,
xyz_coor = np.array([[1.0, 2.0, 10], [3.0, 4.0, 20], [5.0, 6.0, 30], [7.0, 8.0, 40]])
z_coor = xyz_coor[:,2].reshape(4,1)
xyz_coor_nor = xyz_coor/z_coor

# b. Create a 3x3 ndarray. Use fancy indexing to slice out the diagonal elements.
array_33 = np.random.rand(3,3)
array_ind = np.diag_indices(3)
array_33_diag = array_33[array_ind]

# c. Generate a 10 x 3 array of random numbers (all between 0 and 1). From each row, 
# pick the number closest to 0.75. Make use of np.abs and np.argmax to find the column j 
# which contains the closest element in each row.

array_103 = np.random.rand(10,3)
array_103_75 = 0.75*np.ones([10,3])
array_103_diff_abs = np.abs(array_103 - array_103_75)
col_ind = np.argmax(array_103_diff_abs, axis=1)

# d. Predict and verify the shape of the following slicing operation.
x = np.empty((10, 8, 6))

idx0 = np.zeros((3, 8)).astype(int)
idx1 = np.zeros((3, 1)).astype(int)
idx2 = np.zeros((1, 1)).astype(int)

# e. Very Advanced Construct an array:
x = np.arange(12, dtype=np.int32).reshape((3, 4))
array_n22 = np.lib.stride_tricks.as_strided(x, (2,3,2,2), (16,4,16,4), writeable=False)
print(array_n22)