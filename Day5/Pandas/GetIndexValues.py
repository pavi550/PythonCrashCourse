# get index and values of series
import pandas as pd
import numpy as np

ser1 = pd.Series({"India": "New Delhi",
                  "Japan": "Tokyo",
                  "UK": "London"})

print(ser1.values)
print(ser1.index)

print("\n")

ser2 = pd.Series(np.random.normal(size=5))
print(ser2.index)
print(ser2.values)