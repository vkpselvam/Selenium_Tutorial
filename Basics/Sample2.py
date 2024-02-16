import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://www.lambdatest.com/blog/locators-in-selenium-webdriver-with-examples/")
driver.implicitly_wait(10)
driver.maximize_window()
t1=driver.title
print(t1)
t2=driver.find_element(By.LINK_TEXT, "Selenium Locators Tutorial").text
print(t2)
t3=driver.find_element(By.PARTIAL_LINK_TEXT, "Locators Tutorial").text
print(t3)
driver.find_element(By.LINK_TEXT, "Get Started Free").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@placeholder='Business Email*']").send_keys("vinodh.cse.05@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@placeholder='Desired Password*']").send_keys("Ven1@vindh")
time.sleep(2)

