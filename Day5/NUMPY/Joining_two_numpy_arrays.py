# Joining two numpy arrays

import numpy as np

# vertical stack
n1 = np.array([10,20,30,40])
print("Original array n1:\n",n1)
print(n1.shape)
n2 = np.array([50,60,70,80])
print("Original array n2:\n",n2)
print(n2.shape)
n3 = np.vstack((n2,n1))
print("np.vstack((n2,n1)):\n",n3)
print(n3.shape)
print("np.vstack((n1,n2)):\n",np.vstack((n1,n2)))