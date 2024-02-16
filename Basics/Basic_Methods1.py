import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

p=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=p)
driver.get("http://register.rediff.com/register/register.php?FormName=user_details")
driver.maximize_window()
driver.implicitly_wait(30)
female_radio=driver.find_element(By.XPATH,"//input[@value='f']")
print(female_radio.is_selected())
print(female_radio.is_displayed())
print(female_radio.is_enabled())
print("==================")
male_radio=driver.find_element(By.XPATH,"//input[@value='m']")
print(male_radio.is_selected())
print(male_radio.is_displayed())
print(male_radio.is_enabled())

mob_txt=driver.find_element(By.ID,"mobno")

attr_value=mob_txt.get_attribute("name")
print(attr_value)

mob_txt.send_keys("8764437689")
time.sleep(5)

typed_text=mob_txt.get_attribute("value")
print(typed_text)

fsize=mob_txt.value_of_css_property("font-size")
print(fsize)