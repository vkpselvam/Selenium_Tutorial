import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service

s=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\edgedriver_win64\\msedgedriver.exe")
driver=webdriver.Edge(service=s)
driver.get("http://www.google.com")
driver.maximize_window()
time.sleep(5)
driver.minimize_window()
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.close()
