#create a python file app
#file app.py
import Sales
import Finance

print("Calling from Sales")
Sales.display()

print("Calling from Finance")
Finance.display()

from Sales import display,Sales_rpt

print("Calling from Sales")
display()
Sales_rpt()

import Sales as sales

print("Calling from Sales")
sales.display()

# execute app.py