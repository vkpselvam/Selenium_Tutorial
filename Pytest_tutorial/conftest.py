import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager



@pytest.fixture(params=['edge', 'firefox', 'chrome'], scope='class')
def init_driver1(request):
    global web_driver
    if request.param == "edge":
        s = Service(EdgeChromiumDriverManager().install())
        web_driver = webdriver.Edge(service=s)
    if request.param == "firefox":
        s = Service(GeckoDriverManager().install())
        web_driver = webdriver.Firefox(service=s)
    request.cls.driver = web_driver
    if request.param == "chrome":
        s = Service(ChromeDriverManager().install())
        web_driver = webdriver.Chrome(service=s)
    yield
    web_driver.close()
