import time

import selenium.webdriver
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

p=Service(executable_path="C:\\Users\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\geckodriver-v0.32.2-win-aarch64\\geckodriver.exe")
driver=webdriver.Firefox(service=p)
driver.get("http://www.gmail.com")