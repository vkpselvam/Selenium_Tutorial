import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

p=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=p)
driver.implicitly_wait(30)
driver.delete_all_cookies()
driver.get("https://www.fb.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[starts-with(@id,'u_0_0_')]").click()
driver.find_element(By.ID,"privacy-link").click()
pw=driver.current_window_handle
handles=driver.window_handles
print(len(handles))

for x  in range(len(handles)):
    if handles[x]!=driver.current_window_handle:
        driver.switch_to.window(handles[x])
        print(driver.title)
        cwtext=driver.find_element(By.XPATH, "//span[text()='Privacy Centre']").text
        print(cwtext)
        driver.close()
time.sleep(2)
driver.switch_to.window(pw)
driver.find_element(By.NAME,"firstname").send_keys("abcd")
time.sleep(2)