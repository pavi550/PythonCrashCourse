# file: Sales.py
# creating a logger object
import logging

# creating a logger object
logger = logging.getLogger(__name__)

# Note: when we create logger object use that object
# to log the info or details

logging.basicConfig(filename='sales.log',level=logging.INFO,format='%(levelname)s : %(message)s')

""" here still the basic Config will work as it follows he hierarchy"""

def display():
    logger.info("This is display method from sales")

def Sales_rpt():
    logger.info("This is report from sales")

display()

Sales_rpt()
