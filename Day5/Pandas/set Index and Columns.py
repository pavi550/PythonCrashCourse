# set Index and Columns
import pandas as pd

employees = pd.DataFrame(
    data={'Name': ['John Doe', 'William Spark'],
          'Occupation': ['Chemist', 'Statistician'],
          'Date Of Join': ['2018-01-25', '2018-01-26'],
          'Age': [23, 24]},
    index=['Emp001', 'Emp002'],
    columns=['Name', 'Occupation', 'Date Of Join', 'Age'])

print(employees)