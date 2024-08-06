from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.binary_location = "'/oem/home/emdadm/scripts/chrome-linux64/chrome'"    #chrome binary location specified here
chrome_options.add_argument("--start-maximized") #open Browser in maximized mode
chrome_options.add_argument("--no-sandbox") #bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

username = 'elastic'
password = 'elastic'

def journey():
	driver = webdriver.Chrome(options=chrome_options, executable_path='/oem/home/emdadm/scripts/chromedriver-linux64/chromedriver')
	driver.get ("https://elasticsearch-astap.oraclecorp.com/listing")
    delay = 10 # seconds
    #wait until username and password input forms load
    try:
       #enter username and password
       driver.find_element("id", "Username").send_keys(username)
       driver.find_element("id", "Password").send_keys(password)
       #click sign in
       driver.find_element("id", "Sign in").click()
    except:
        return "STATUS_DOWN"
        driver.close()
    else:
        return "STATUS_UP"
        
print(journey())