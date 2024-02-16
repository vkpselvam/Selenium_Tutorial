import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obt=Options()
obt.add_argument("--disable-notifications")
p=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=p,options=obt)
driver.get("https://www.spicejet.com")
driver.maximize_window()
driver.implicitly_wait(30)
time.sleep(10)
