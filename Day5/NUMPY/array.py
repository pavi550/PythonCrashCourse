import numpy as np

thearray = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print("Before:",thearray)
thearray = thearray.reshape(2, 4)
print("thearray.reshape(2, 4):\n",thearray)

print("********" * 10)
thearray = thearray.reshape(4, 2)
print("thearray.reshape(4, 2):\n",thearray)

print("********" * 10)
thearray = thearray.reshape(8, 1)
print("thearray.reshape(8, 1):\n",thearray)