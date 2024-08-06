# Eve Rosenthal
# script to log in and out of gmail

import config
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
#from chromedriver_py import binary_path # this will get you the path variable
#svc = webdriver.ChromeService(executable_path="/usr/local/lib/python3.6/site-packages/chromedriver")
#driver = webdriver.Chrome(service=svc)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')

username = config.username
password = config.password

def journey():
    try:
        driver = webdriver.Chrome(executable_path="./chromedriver-linux64/chromedriver", chrome_options=chrome_options)
        driver.get("https://mail.google.com/mail/u/0/")
        delay = 10 # seconds
        #wait until username and password input forms load
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'identifierId')))
        #enter username and password
        driver.find_element("id", "identifierId").send_keys(username)
        print("Submitted username")
        driver.find_element(By.ID, "identifierNext").click()
        myElem = WebDriverWait(driver, delay).until(EC.visibility_of_element_located((By.ID, 'password')))
        myElem = driver.find_element(By.ID, 'password').send_keys(password)
        #click sign in
        print("Submitted password")
        driver.find_element(By.ID, "passwordNext").click()
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//a[@class=\"gb_d gb_Da gb_H\"]")))
        print("Logged in successfully")
        driver.find_element(By.XPATH, "//a[@class=\"gb_d gb_Da gb_H\"]").click()
        driver.switch_to.frame("account")
        driver.find_element(By.XPATH, "//*[contains(text(), 'Sign out')]").click()
        print("Clicked log out")
        print("Logged out successfully")
        driver.close()
        return "STATUS_UP"
    except:
        return "STATUS_DOWN"
print(journey())