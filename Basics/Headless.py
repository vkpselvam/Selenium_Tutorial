import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
opt=Options()
opt.add_argument('--headless')
s=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=s, options=opt)
driver.get("http://www.facebook.com")
driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"html/body/div/div[1]/div/div/div/div/div[2]/div/div/form/div/div/input").send_keys("vino")
time.sleep(5)
text1=driver.find_element(By.XPATH,"html/body/div/div/div/div/div/div/div/h2").text
print(text1)
time.sleep(5)
print(driver.title)
print(driver.current_url)
print('browser closed')