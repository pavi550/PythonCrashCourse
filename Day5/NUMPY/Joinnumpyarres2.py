# Joining two numpy arrays

import numpy as np

#  column stack
n1 = np.array([10,20,30,40])
print("Original array n1:\n",n1)
print(n1.shape)
n2 = np.array([50,60,70,80])
print("Original array n2:\n",n2)
print(n2.shape)
n3 = np.column_stack((n2,n1))
print("np.column_stack((n2,n1)):\n",n3)
print(n3.shape)
print("np.column_stack((n1,n2)):\n",np.column_stack((n1,n2)))