# script to log in and out of a url

import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.binary_location = '/oem/home/emdadm/scripts/chrome-linux64/chrome'

username = 'elastic'
password = 'elastic'

def journey():
    driver = webdriver.Chrome(executable_path='/oem/home/emdadm/scripts/chromedriver-linux64/chromedriver', options=chrome_options)
    driver.get("https://elasticsearch-astap.oraclecorp.com/listing")
    delay = 10 # seconds
    #wait until username and password input forms load
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'idcs-signin-basic-signin-form-username')))
        #enter username and password
        driver.find_element("id", "idcs-signin-basic-signin-form-username").send_keys(username)
        driver.find_element("id", "idcs-signin-basic-signin-form-password").send_keys(password)
        #click sign in
        driver.find_element("id", "idcs-signin-basic-signin-form-submit").click()
        #wait until cssem homepage loads
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'emT:pref')))
        #click username
        driver.find_element("id", "emT:pref").click()
        #wait until dropdown loads
        myElem = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.ID, 'emT:file_log_out')))
        #click logout
        driver.find_element("id", "emT:file_log_out").click()
    except:
        return "STATUS_DOWN"
        driver.close()
    else:
        return "STATUS_UP"
        
print(journey())