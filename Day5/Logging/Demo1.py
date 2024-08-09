# file Demo1.py
# log info from only 1 file is recorded..
import Sales
import logging

#logging in a file
#Formatting the log message
logging.basicConfig(format='%(asctime)s %(message)s',level=logging.DEBUG)

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

a = 20
b = 5

Add_result = add(a,b)
logging.debug("Addition: {} + {} is {} : ".format (a,b, Add_result))

Sub_result = sub(a,b)
logging.debug("Subtraction: {} - {} is {} : ".format (a,b, Sub_result))

Sales.display()