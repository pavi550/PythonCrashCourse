# file: Sales.py
# configure custom logger
import logging

# creating a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# configuring file formatting
formatter = logging.Formatter('%(levelname)s : %(message)s')
#add the formatter to the file handler (just after file handler)

# to log the data in file we will configure fileHandler
file_handler = logging.FileHandler('Sales.log')
file_handler.setFormatter(formatter)

# we need to add file_handler to the logger
logger.addHandler(file_handler)

#logging.basicConfig(filename='sales.log',level=logging.INFO,format='%(levelname)s : %(message)s')


def display():
    logger.info("This is display method from sales")

def Sales_rpt():
    logger.info("This is report from sales")

display()

Sales_rpt()