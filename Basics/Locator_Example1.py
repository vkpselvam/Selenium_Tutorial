import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("http://www.facebook.com")
driver.maximize_window()
driver.delete_all_cookies()
#using id  locator
driver.find_element(By.ID,"email").send_keys("Admin")
time.sleep(5)


#using name locator
driver.find_element(By.NAME, "pass").send_keys("admin123")
time.sleep(5)

#using class name
fbtext=driver.find_element(By.CLASS_NAME,"_8eso").text
print(fbtext)
time.sleep(5)


#using linktext
fp=driver.find_element(By.LINK_TEXT,"Forgotten password?").text
print(fp)
time.sleep(5)

#using partiallinktext
fp1=driver.find_element(By.PARTIAL_LINK_TEXT,"gotten").text
print(fp1)