# create and print DataFrame


import pandas as pd

employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002'],
    'Name': ['John Doe', 'William Spark'],
    'Occupation': ['Chemist', 'Statistician'],
    'Date Of Join': ['2018-01-25', '2018-01-26'],
    'Age': [23, 24]})

print(employees)