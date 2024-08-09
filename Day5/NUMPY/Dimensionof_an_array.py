# Dimension of an array
import numpy as np

array1d = np.array([1, 2, 3, 4, 5, 6])
print("The dimension: ", array1d.ndim)  # 1
print("*********"*4)
array2d = np.array([[1, 2, 3], [4, 5, 6]])
print("The dimension: ", array2d.ndim)  # 2
print("*********"*4)
array3d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
array3d = array3d.reshape(2, 3, 2)
print("The dimension: ", array3d.ndim)  # 3
print(array3d)