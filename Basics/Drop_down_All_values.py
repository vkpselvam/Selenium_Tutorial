import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://www.facebook.com")
driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(30)
driver.find_element(By.XPATH, "//a[starts-with(@id,'u_0_0_')]").click()
time.sleep(5)
month_dd = driver.find_element(By.ID, "month")
sel = Select(month_dd)
all_dd = sel.options
print(len(all_dd))
'''
for i in all_dd:
    if i.text =="Jul":
        sel.select_by_index(i)
        break
'''
for i in  all_dd:
    print(i.text)

time.sleep(5)