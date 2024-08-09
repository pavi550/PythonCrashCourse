# Addition of two numpy arrays

import numpy as np

n1 = np.array([10,20,30,40])
print("Original array n1:\n",n1)
print(n1.shape)
n2 = np.array([50,60,70,80])
print("Original array n2:\n",n2)
print(n2.shape)
n3 = np.sum([n2,n1])
print("np.sum([n2,n1]):\n",n3)
print(n3.shape)
# Adding the column values using the axis
n3 = np.sum([n1,n2],axis = 0)
print("np.sum([n1,n2],axis = 0):\n",n3)
n3 = np.sum([n1,n2],axis = 1)
print("np.sum([n1,n2],axis = 1):\n",n3)