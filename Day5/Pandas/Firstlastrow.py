# get the first or last few rows from a Series

import pandas as pd

values = ["India", "Canada", "Australia",
          "Japan", "Germany", "France"]

code = ["IND", "CAN", "AUS", "JAP", "GER", "FRA"]

ser1 = pd.Series(values, index=code)

print("-----Head()-----")
print(ser1.head())

print("\n\n-----Head(2)-----")
print(ser1.head(2))