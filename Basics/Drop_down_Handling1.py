import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("http://www.facebook.com")
driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//a[starts-with(@id,'u_0_0_')]").click()
time.sleep(5)
month_dd=driver.find_element(By.ID, "month")
sel=Select(month_dd)
sel.select_by_visible_text("Aug")
time.sleep(5)
sel.select_by_value("12")
time.sleep(5)
sel.select_by_index(1)
time.sleep(5)