import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

p=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=p)
driver.implicitly_wait(30)
driver.get("https://www.rediff.com/")
driver.maximize_window()
driver.delete_all_cookies()
time.sleep(2)
driver.find_element(By.XPATH, "//html//body//div[2]//div//div[3]//p//a[2]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//html//body//center//form//div//table[2]//tbody//tr[3]//td[3]//input").send_keys("vinothkumar")
time.sleep(2)
driver.find_element(By.XPATH,"//html//body//center//form//div//table[2]//tbody//tr[7]//td[3]//input").send_keys("vkpselvam")
time.sleep(3)
driver.find_element(By.XPATH,"//html//body//center//form//div//table[2]//tbody//tr[9]//td[3]//input").send_keys("abcd1234")
time.sleep(2)
driver.find_element(By.XPATH,"//html//body//center//form//div//table[2]//tbody//tr[11]//td[3]//input").send_keys("abcd1234")
time.sleep(2)
driver.find_element(By.XPATH,"//html//body//center//form//div//table[2]//tbody//tr[14]//td//div//table//tbody//tr//td[3]//input").send_keys("vkumar@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"//html//body//center//form//div//table[2]//tbody//tr[20]//td//div//table/tbody//tr//td[3]//div[3]//input").send_keys("9876543210")
time.sleep(2)
month_dd=driver.find_element(By.NAME, "DOB_Month")
sel=Select(month_dd)
sel.select_by_visible_text("Mar")
