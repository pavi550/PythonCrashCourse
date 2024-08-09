# Get Length Size and Shape of a Series

import pandas as pd

values = ["India", "Canada", "Australia",
          "Japan", "Germany", "France"]

code = ["IND", "CAN", "AUS", "JAP", "GER", "FRA"]

ser1 = pd.Series(values, index=code)

print(len(ser1))

print(ser1.shape)

print(ser1.size)