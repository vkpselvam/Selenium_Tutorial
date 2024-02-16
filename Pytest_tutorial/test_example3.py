import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest

from webdriver_manager.chrome import ChromeDriverManager

def test_fb():
    p = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=p)
    driver.get("http://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    assert driver.title == "Facebook – log in or sign up"
    time.sleep(5)
    driver.close()

def test_google():
    p = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=p)
    driver.get("http://www.google.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    assert driver.title == "Google"
    time.sleep(5)
    driver.close()

def test_flipkart():
    p = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=p)
    driver.get("http://www.flipkart.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    assert driver.title == "Flipkart"
    time.sleep(5)
    driver.close()

def test_rediff():
    p = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=p)
    driver.get("http://www.rediff.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    assert driver.title == "Rediff"
    time.sleep(5)
    driver.close()