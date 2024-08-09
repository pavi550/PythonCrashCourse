# Iterate over rows and columns
import pandas as pd

employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})

print("\n Example iterrows \n")
for index, col in employees.iterrows():
    print(col['Name'], "--", col['Age'])

print("\n Example itertuples \n")
for row in employees.itertuples(index=True, name='Pandas'):
    print(getattr(row, "Name"), "--", getattr(row, "Age"))
