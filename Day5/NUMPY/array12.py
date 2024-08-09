import numpy as np

array1 = np.zeros(3,dtype=int)
print("np.zeros(3):\n",array1)
print(array1.dtype)
array3 = np.zeros((3,3),dtype=int)
print("np.zeros((3,3)):\n",array3)
print(array3.dtype)
array2 = np.ones(3,dtype=int)
print("np.ones(3):\n",array2)
print(array2.dtype)
array1 = np.zeros((5,5))
print("np.zeros((5,5)):\n",array1)