import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("http://www.facebook.com")
driver.maximize_window()
time.sleep(5)
driver.minimize_window()
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.close()