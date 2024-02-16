import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

p=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=p)
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.switch_to.frame(0)
src_ele=driver.find_element(By.ID,"draggable")
tar_ele=driver.find_element(By.ID,"droppable")
act=ActionChains(driver)
act.drag_and_drop(src_ele,tar_ele).perform()
time.sleep(10)