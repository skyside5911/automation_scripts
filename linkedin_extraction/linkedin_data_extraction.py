from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from fake_headers import Headers
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
driver_path='C:\\browserdrivers\\chromedriver.exe'
# driver_path=r'/usr/bin/chromedriver'
#sitepath="D:\\work\\python\\webscrape\\"
header = Headers(
    browser="chrome",  # Generate only Chrome UA
    os="win",  # Generate only Windows platform
    headers=False # generate misc headers
)

chrome_options = Options()
chrome_options.add_argument("--user-agent={customUserAgent}")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')
#driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
s = Service(driver_path) 
options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=chrome_options, service=s)
url = "https://www.linkedin.com/login"
driver.get(url)
sleep(2)
email_field = driver.find_element(By.ID,'username')
driver.find_element(By.ID,'username').clear()
driver.find_element(By.ID,'username').send_keys("jasbarnissing@gmail.com")
sleep(4)
password_field = driver.find_element(By.ID,'password')
driver.find_element(By.ID,'password').clear()
driver.find_element(By.ID,'password').send_keys("jasbarnissing1")      
sleep(2)
login_field = driver.find_element(by=By.XPATH, value="/html/body/div/main/div[2]/div[1]/form/div[3]/button").click()
sleep(3)
