# Eve Rosenthal
# script to log in and out of a url

import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

username = "eve.rosenthal@oracle.com"
password = "ElPsyKongroo8*"

def login_logout():
    driver = webdriver.Chrome()
    driver.get("https://cssem.appoci.oraclecorp.com/em")
    delay = 10 # seconds
    #wait until username and password input forms load
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'idcs-signin-basic-signin-form-username')))
    time.sleep(2)
    #enter username and password
    driver.find_element("id", "idcs-signin-basic-signin-form-username").send_keys(username)
    driver.find_element("id", "idcs-signin-basic-signin-form-password").send_keys(password)
    #click sign in
    driver.find_element("id", "idcs-signin-basic-signin-form-submit").click()
    #wait until cssem homepage loads
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'emT:pref')))
    #click username
    driver.find_element("id", "emT:pref").click()
    time.sleep(2)
    #wait until dropdown loads
    myElem = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.ID, 'emT:file_log_out')))
    #click logout
    driver.find_element("id", "emT:file_log_out").click()
    time.sleep(5)
    driver.close()
    return "STATUS_UP"

print(login_logout())