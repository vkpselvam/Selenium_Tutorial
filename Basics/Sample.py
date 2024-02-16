import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

p1=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=p1)
driver.get("https://www.facebook.com/")
driver.implicitly_wait(20)
time.sleep(3)
driver.maximize_window()
t3=driver.title
print(t3)
t4=driver.current_url
print(t4)
driver.refresh()
t=driver.find_element(By.CLASS_NAME,"_8eso").text
print(t)
t2=driver.find_element(By.CLASS_NAME, "_58mk").text
print(t2)
time.sleep(5)
t5=driver.find_element(By.LINK_TEXT, "Forgotten password?").text
print(t5)
driver.find_element(By.XPATH, "//a[@data-testid='open-registration-form-button']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Sindhu")
driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Shanmugam")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@name='reg_email__']").send_keys("8971189105")
driver.find_element(By.XPATH, "//input[@data-type='password']").send_keys("Sinu24")
time.sleep(3)
driver.find_element(By.XPATH, "//select[@id='day']").send_keys(5)
driver.find_element(By.XPATH, "//select[@id='month']").send_keys("Nov")
driver.find_element(By.XPATH, "//select[@id='year']").send_keys("1989")
time.sleep(4)
driver.find_element(By.XPATH, "//input[@class='_8esa'][@name='sex'][@value='2']").click()
time.sleep(2)
driver.find_element(By.NAME, "websubmit").click()
time.sleep(2)