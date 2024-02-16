import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(30)
time.sleep(5)
driver.execute_script("window.scrollBy(0,1000)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,-1000)")
time.sleep(5)