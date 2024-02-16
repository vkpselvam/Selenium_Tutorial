import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

p=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=p)
driver.get("https://www.fb.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[starts-with(@id,'u_0_0_')]").click()
WebDriverWait(driver,timeout=10).until(EC.presence_of_element_located((By.NAME,"firstname"))).send_keys("Ram")

time.sleep(7)



'''
what is immplicitly_wait ?
Driver can wait for a particular time to load all the webelements into the webpage is called implicitly wait.

What is Explicitly wait?

Driver can wait for a particular time to load particular webelement into the webpage is called Explicitly wait.
'''