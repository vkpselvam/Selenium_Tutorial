from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://www.facebook.com")
driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(30)
driver.save_screenshot("C:\\Users\\MyPc\\Desktop\\Screenshot\\test2.jpeg")

