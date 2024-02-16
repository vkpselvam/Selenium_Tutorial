import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

p=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=p)
driver.implicitly_wait(30)
driver.get("https://www.rediff.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//a[@title='Create Rediffmail Account']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//input[contains(@name, 'name')][contains(@maxlength, '61')]").send_keys("vinothkumar")
time.sleep(2)
driver.find_element(By.XPATH,"//input[contains(@name,'login')]").send_keys("vkkamly")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='newpasswd']").send_keys("Kunthini123")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='newpasswd1']").send_keys("Kunthini123")
time.sleep(2)
driver.find_element(By.XPATH, "//input[contains(@name, 'altemail')][contains(@maxlength, '100')]").send_keys("abcd@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='mobno']").send_keys("9535444500")
time.sleep(2)
driver.find_element(By.XPATH, "//input[contains(@name, 'gender')][contains(@value, 'm')]").click()
time.sleep(2)
driver.find_element(By.ID, "country").send_keys("india")
time.sleep(2)
driver.find_element(By.XPATH, "//select[contains(@name, 'city')]").send_keys("salem")
time.sleep(2)

