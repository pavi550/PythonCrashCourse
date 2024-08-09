# Drop DataFrame Column(s) by Name and Index:
import pandas as pd

employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})

print(employees)

print("\n Drop Column by Name \n")
employees.drop('Age', axis=1, inplace=True)
print(employees)

print("\n Drop Column by Index \n")
employees.drop(employees.columns[[0, 1]], axis=1, inplace=True)
print(employees)