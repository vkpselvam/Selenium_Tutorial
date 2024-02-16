import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

p=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=p)
driver.get("https://www.rediff.com")
driver.maximize_window()
driver.implicitly_wait(30)
wp_text=driver.find_element(By.XPATH,"//a[@title='Lightning fast business email hosting']").text
print(wp_text)
#driver.switch_to.frame("moneyiframe")  #BY NAME
#driver.switch_to.frame(0) #By index
f1=driver.find_element(By.XPATH,"//iframe[@title='Rediff Money Widget']")
driver.switch_to.frame(f1)
frame_text=driver.find_element(By.XPATH,"//span[text()='NSE']").text
print(frame_text)
driver.switch_to.default_content()
wp_text1=driver.find_element(By.XPATH,"//a[@title='Lightning fast business email hosting']").text
print(wp_text1)