# Slicing a Series into subsets

import pandas as pd

num = [000, 100, 200, 300, 400, 500, 600, 700, 800, 900]

idx = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

series = pd.Series(num, index=idx)

print("\n [2:2] \n")
print(series[2:4])

print("\n [1:6:2] \n")
print(series[1:6:2])

print("\n [:6] \n")
print(series[:6])

print("\n [4:] \n")
print(series[4:])

print("\n [:4:2] \n")
print(series[:4:2])

print("\n [4::2] \n")
print(series[4::2])

print("\n [::-1] \n")
print(series[::-1])