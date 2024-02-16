from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

p=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=p)
driver.implicitly_wait(30)
driver.delete_all_cookies()
driver.get("https://www.rediff.com/")
driver.maximize_window()
list1=driver.find_elements(By.TAG_NAME,"a")
print(len(list1))

for i in list1:
    print(i.text,"--->", i.get_attribute("href"))