import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("http://www.facebook.com")
driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(30)
#single attribute
driver.find_element(By.XPATH,"//input[@placeholder='Email address or phone number']").send_keys("admin123")

driver.find_element(By.XPATH,"//input[@class='inputtext _55r1 _6luy']").clear()

driver.find_element(By.XPATH,"//input[@aria-label='Email address or phone number']").send_keys("Vino")

#text()

t1=driver.find_element(By.XPATH,"//a[text()='Forgotten password?']").text
print(t1)


#contains text

t2=driver.find_element(By.XPATH,"//a[contains(text(), 'ate n')]").text
print(t2)

#starts-with text
t3=driver.find_element(By.XPATH,"//a[starts-with(text(),'Create n')]").text
print(t3)

#contains attribute

t4=driver.find_element(By.XPATH,"//a[contains(@id, 'u_0_0')]").text
print(t4)

#Starts-with attribute
t5=driver.find_element(By.XPATH,"//a[starts-with(@id, 'u_0_0')]").text
print(t5)

time.sleep(5)
driver.find_element(By.XPATH,"//a[@data-testid='open-registration-form-button']").click()


#Multiple attribute
driver.find_element(By.XPATH," //input[@class='_8esa'][@value='2']").click()
time.sleep(5)