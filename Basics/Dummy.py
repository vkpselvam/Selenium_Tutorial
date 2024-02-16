from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\MyPc\\Documents\\Software Testing\\Selenium_Drivers\\chromedriver\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/index.htm")
driver.close()