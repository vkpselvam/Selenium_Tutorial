import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://www.facebook.com")
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.get("https://www.google.com")
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
driver.refresh()
time.sleep(5)
actual_title=driver.title
print(actual_title)
time.sleep(5)
actual_url=driver.current_url
print(actual_url)
time.sleep(5)
driver.minimize_window()
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.close()