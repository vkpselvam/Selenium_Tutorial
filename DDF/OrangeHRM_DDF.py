from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import Utility_DDF

s=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=s)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(30)
path="C:\\Users\\MyPc\\Desktop\\DDF.xlsx"

rows=Utility_DDF.getRow_count(path,"Sheet3")

for r in range(2, rows+1):

    username=Utility_DDF.read_data(path,"Sheet3",r, 1)
    password=Utility_DDF.read_data(path,"Sheet3",r,2)

    driver.find_element(By.NAME,"username").send_keys(username)
    driver.find_element(By.NAME,"password").send_keys(password)
    driver.find_element(By.XPATH,"//button[normalize-space(text='Login')] ").click()
    driver.find_element(By.CLASS_NAME, "oxd-dialog-close-button oxd-dialog-close-button-position").click()
    homepagetitle=driver.title

    if homepagetitle == "OrangeHRM":
        Utility_DDF.write_data(path,"Sheet3",r,3,"Pass")
        driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
        driver.find_element(By.CLASS_NAME, "oxd-userdropdown-link").click()

    else:
        Utility_DDF.write_data(path, "Sheet3", r, 3, "Fail")
        driver.close()