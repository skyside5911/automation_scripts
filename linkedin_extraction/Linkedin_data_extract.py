from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
driver_path='C:\\browserdrivers\\chromedriver.exe'
driver = webdriver.Chrome(options=chrome_options, service=driver_path)
driver.get("https://www.linkedin.com/login")