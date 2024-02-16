import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

p=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=p)
driver.get("https://money.rediff.com/gainers")
driver.maximize_window()
driver.implicitly_wait(30)
t1=driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr[5]/td[1]").text
print(t1)

t2=driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr[5]").text
print(t2)

li=driver.find_elements(By.XPATH,"//table[@class='dataTable']/tbody/tr")

print(len(li))

for i in li:
    print(i.text)