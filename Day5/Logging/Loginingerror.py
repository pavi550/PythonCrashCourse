# Logging  Error or Exception
import Sales
import logging

# creating a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# configuring file formatting
formatter = logging.Formatter('%(asctime)s:%(name)s: %(message)s')
#add the formatter to the file handler (just after file handler)

# to log the data in file we will configure fileHandler
file_handler = logging.FileHandler('test.log')
file_handler.setFormatter(formatter)

# we need to add file_handler to the logger
logger.addHandler(file_handler)
#Formatting the log message
logging.basicConfig(format='%(asctime)s %(message)s',level=logging.DEBUG)

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def div(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        logger.error("Tried to divide by 0")
    else:
        return result

a = 20
b = 0
Div_result = div(a,b)
logger.debug("Divide: {} - {} is {} : ".format (a,b, Div_result))

Add_result = add(a,b)
logger.debug("Addition: {} + {} is {} : ".format (a,b, Add_result))

Sub_result = sub(a,b)
logger.debug("Subtraction: {} - {} is {} : ".format (a,b, Sub_result))

Sales.display()