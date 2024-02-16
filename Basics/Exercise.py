import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

p=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=p)
driver.get("https://www.w3schools.com/python/python_intro.asp")
driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(30)
time.sleep(5)
driver.find_element(By.XPATH, "//html//body//div[6]//div[1]//div[1]//a[3]").click()
time.sleep(5)
