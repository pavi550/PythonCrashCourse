# Eve Rosenthal and Praveen Kumar
# script to log in and out of myhelp

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pyotp
from selenium.webdriver.chrome.options import Options

sso_username = "praveen.av.kumar@oracle.com"
sso_password = "Belcome@ggvt12345"

chrome_options = Options()
chrome_options.add_argument('--headless')

def get_two_factor_code():
    secret = "6NORLSKPHAXYX3NED34LHIATBM"
    totp = pyotp.TOTP(secret)
    two_factor_code = totp.now()
    return two_factor_code

def journey():
   
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://myhelp.oracle.com/app/home")
    delay = 20 # seconds
    #wait until username and password input forms load
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'idcs-signin-basic-signin-form-username')))
    #enter username and password
    driver.find_element(By.ID, "idcs-signin-basic-signin-form-username").send_keys(sso_username)
    WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.ID, 'idcs-signin-basic-signin-form-submit')))
    driver.find_element(By.ID, 'idcs-signin-basic-signin-form-submit').click()
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'idcs-auth-pwd-input')))
    driver.find_element("id", "idcs-auth-pwd-input").send_keys(sso_password)
    #click sign in
    time.sleep(3)
    driver.find_element(By.ID, "idcs-mfa-mfa-auth-user-password-submit-button").click()
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'idcs-mfa-mfa-auth-passcode-input')))
    token = get_two_factor_code()
    # enter the token in the UI
    time.sleep(2)
    driver.find_element(By.ID, "idcs-mfa-mfa-auth-passcode-input").send_keys(token)
    time.sleep(2)
    driver.find_element(By.ID, 'idcs-mfa-mfa-auth-totp-submit-button').click()
    time.sleep(10)
    driver.close()

journey()