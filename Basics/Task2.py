import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://demo.guru99.com/test/newtours/")
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://demo.guru99.com/test/newtours/register.php")
driver.maximize_window()
time.sleep(5)
#using id  locator

driver.find_element(By.NAME,"firstName").send_keys("VKR")
time.sleep(5)

driver.find_element(By.NAME,"lastName").send_keys("SELVAM")
time.sleep(1)

driver.find_element(By.NAME,"phone").send_keys(9535444500)
time.sleep(1)

driver.find_element(By.ID,"userName").send_keys("vkpselvam0511@gmail.com")
time.sleep(1)

driver.find_element(By.NAME,"address1").send_keys("2/71A, Rasi Nagar")
time.sleep(1)

driver.find_element(By.NAME,"city").send_keys("Salem")
time.sleep(1)

driver.find_element(By.NAME,"state").send_keys("Tamilnadu")
time.sleep(1)

driver.find_element(By.NAME,"postalCode").send_keys(636030)
time.sleep(1)

driver.find_element(By.TAG_NAME,"select").send_keys("india")
time.sleep(1)


driver.find_element(By.ID,"email").send_keys("Vkpselvam0511@gamil.com")
time.sleep(1)

pass1=driver.find_element(By.NAME,"password").send_keys("ABCD@1234")
time.sleep(1)

pass2=driver.find_element(By.NAME,"confirmPassword").send_keys("ABCD@1234")
time.sleep(5)

