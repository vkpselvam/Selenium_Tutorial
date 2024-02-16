import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(30)

driver.find_element(By.NAME,"proceed").click()
time.sleep(10)
alt=driver.switch_to.alert
alert_text=alt.text
print(alert_text)
#alt.dismiss()
alt.accept()
time.sleep(5)