import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

p=Service(executable_path="D:\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=p)
driver.get("https://www.rediff.com")
driver.maximize_window()
driver.implicitly_wait(30)
li=driver.find_elements(By.TAG_NAME, "iframe")
print(len(li))
for i in li:
    print(i.get_attribute("id"),"--->",i.get_attribute("name"))
    time.sleep(10)