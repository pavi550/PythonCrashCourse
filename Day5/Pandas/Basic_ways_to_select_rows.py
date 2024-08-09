# Basic ways to select rows

import pandas as pd

employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})

print("\nUse == operator\n")
print(employees.loc[employees['Age'] == 23])

print("\nUse < operator\n")
print(employees.loc[employees['Age'] < 30])

print("\nUse != operator\n")
print(employees.loc[employees['Occupation'] != 'Statistician'])

print("\nMultiple Conditions\n")
print(employees.loc[(employees['Occupation'] != 'Statistician') &
                    (employees['Name'] == 'John')])