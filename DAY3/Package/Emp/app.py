#create a python file app
#file app.py
import Emp.Sales
import Emp.Finance

print("Calling from Sales")
Emp.Sales.display()

print("Calling from Finance")
Emp.Finance.display()

from Emp.Sales import display,Sales_rpt

print("Calling from Sales")
display()
Sales_rpt()

import Emp.Sales as sales

print("Calling from Sales")
sales.display()

# execute app.py