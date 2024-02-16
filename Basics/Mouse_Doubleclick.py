import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

p=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=p)
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
driver.implicitly_wait(30)
ele_dd=driver.find_element(By.XPATH,"//button[text()='Double-Click Me To See Alert']")
act=ActionChains(driver)
act.double_click(ele_dd).perform()
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(10)