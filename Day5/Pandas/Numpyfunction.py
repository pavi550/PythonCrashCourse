# using NumPy functions:

import pandas as pd
import numpy as np

ser1 = pd.Series(np.linspace(1, 10, 5))
print(ser1)

ser2 = pd.Series(np.random.normal(size=5))
print(ser2)