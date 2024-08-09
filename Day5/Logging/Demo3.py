# file Demo1.py

import Sales3
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
logging.info("Addition: {} + {} is {} : ".format (a,b, Add_result))

Sub_result = sub(a,b)
logging.info("Subtraction: {} - {} is {} : ".format (a,b, Sub_result))

Sales3.display()