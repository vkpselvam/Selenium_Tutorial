import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

p=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=p)
driver.get("https://www.fb.com/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//a[starts-with(@id,'u_0_0_')]").click()
driver.find_element(By.NAME,"firstname").send_keys("Ram")
time.sleep(7)