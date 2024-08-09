# file: Sales.py

import logging

logging.basicConfig(filename='sales.log',level=logging.INFO,format='%(levelname)s : %(message)s')

def display():
    logging.info("This is display method from sales")

def Sales_rpt():
    logging.info("This is report from sales")

display()

Sales_rpt()