import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s=Service(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://www.rahulshettyacademy.com/")
time.sleep(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(2)
driver.implicitly_wait(30)

driver.find_element(By.XPATH, "html//body//div//div//fieldset//label[1]//input").click()
time.sleep(2)
driver.find_element(By.XPATH, "html//body//div//div//fieldset//label[2]//input").click()
time.sleep(2)
driver.find_element(By.XPATH, "html//body//div//div//fieldset//label[3]//input").click()
time.sleep(2)
driver.find_element(By.XPATH, '//input[@placeholder="Type to Select Countries"]').send_keys("India")
time.sleep(2)
driver.find_element(By.XPATH, '//select[@id="dropdown-class-example"]').click()
time.sleep(2)
driver.find_element(By.XPATH, "html//body//div[1]//div[3]//fieldset//select//option[2]").click()
time.sleep(2)
driver.find_element(By.XPATH, "html//body//div[1]//div[3]//fieldset//select//option[3]").click()
time.sleep(2)
driver.find_element(By.XPATH, "html//body//div[1]//div[3]//fieldset//select//option[4]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='checkBoxOption1']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='checkBoxOption2']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='checkBoxOption3']").click()
time.sleep(2)
cbox3 = driver.find_element(By.XPATH, "//input[@id='checkBoxOption3']").is_selected()
time.sleep(2)
print(cbox3, "Checkbox 3 is checked")
if cbox3:
    driver.find_element(By.XPATH, "//input[@id='checkBoxOption3']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@id='openwindow']").click()
time.sleep(5)
driver.find_element(By.XPATH, '//a[@id="opentab"]').click()
time.sleep(5)
driver.switch_to.default_content()

# Alert Pop-up

driver.find_element(By.XPATH, '//input[@id="alertbtn"]').click()
time.sleep(5)
alt=driver.switch_to.alert
alert_text=alt.text
print(alert_text)
alt.accept()
time.sleep(5)
driver.find_element(By.XPATH, '//input[@id="confirmbtn"]').click()
time.sleep(5)






