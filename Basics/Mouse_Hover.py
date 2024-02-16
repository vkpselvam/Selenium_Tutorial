import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

p=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=p)
driver.get("https://www.naukri.com")
driver.maximize_window()
driver.implicitly_wait(30)
ele1=driver.find_element(By.XPATH,"//a[@title='Explore top companies hiring on Naukri']")

act=ActionChains(driver)
act.move_to_element(ele1).perform()
time.sleep(10)
