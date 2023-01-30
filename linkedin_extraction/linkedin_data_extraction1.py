import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from fake_headers import Headers
from time import sleep
from bs4 import BeautifulSoup
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
credential = open("id_password.txt")
line = credential.readlines()
username = line[0]
password = line[1]
email_field = driver.find_element(By.ID,'username')
driver.find_element(By.ID,'username').clear()
driver.find_element(By.ID,'username').send_keys(username)
sleep(4)
password_field = driver.find_element(By.ID,'password')
driver.find_element(By.ID,'password').clear()
driver.find_element(By.ID,'password').send_keys(password)      
sleep(2)
login_field = driver.find_element(by=By.XPATH, value="/html/body/div/main/div[2]/div[1]/form/div[3]/button").click()
sleep(3)
# click_on_jobs_button = driver.find_element(by=By.XPATH, value="/html/body/div[5]/header/div/nav/ul/li[3]/a/div/div/li-icon/svg/path").click()
# job_path = driver.find_element(by=By.XPATH, value="/html/body/div[5]/header/div/div/div/div[2]/div[2]/div/div/input[1]").click()
find_search_box = driver.find_element(by=By.XPATH,value='/html/body/div[5]/header/div/div/div/div[1]/input')
driver.find_element(by=By.XPATH,value='/html/body/div[5]/header/div/div/div/div[1]/input').clear()
find_search_box.send_keys("python")
sleep(5)
find_search_box.send_keys(Keys.RETURN)
sleep(5)
uu = requests.get(find_search_box)
page_source = BeautifulSoup(uu.content,"html.parser")
# print(page_source)
profiles = page_source.find_all('a', class_='entity-result__title-line entity-result__title-line--2-lines')
# print(profiles)
sleep(5)
all_profile_urls = []
for profile in profiles:
    profile_id = profile.get("href")
    profile_url = "https://www.linkedin.com/"+profile_id
    sleep(5)
    if profile_url not in all_profile_urls:
        all_profile_urls.append(profile_url)
print(all_profile_urls)


