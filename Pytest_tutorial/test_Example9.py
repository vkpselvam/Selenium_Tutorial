import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(params=['edge','firefox','chrome'], scope='class')
def init_driver(request):
    global web_driver
    if request.param == "edge":
        s=Service(EdgeChromiumDriverManager().install())
        web_driver=webdriver.Edge(service=s)
    if request.param == "firefox":
        s=Service(GeckoDriverManager().install())
        web_driver=webdriver.Firefox(service=s)
    request.cls.driver=web_driver
    if request.param == "chrome":
        s=Service(ChromeDriverManager().install())
        web_driver=webdriver.Chrome(service=s)
    yield
    web_driver.close()

@pytest.mark.usefixtures("init_driver")
class Base_Test:
    pass

class Test_Fb_app(Base_Test):
    def test_verifyTittle(self):
        self.driver.get("http://www.fb.com")
        actual_title = self.driver.title

        assert actual_title == "Facebook – log in or sign up"

    def test_verifyUrl(self):
        actual_url = self.driver.current_url
        assert actual_url == "https://www.facebook.com/"

    def test_verifyHomepage_text(self):
        actual_text = self.driver.find_element(By.CLASS_NAME, "_8eso").text
        assert actual_text == "Facebook helps you connect and share with the people in your life."

    def test_verifyUsername_textbox_enable(self):
        actual_utextbox = self.driver.find_element(By.ID, "email").is_enabled()

        assert actual_utextbox == False

    def test_verifyUsername_textbox_display(self):
        actual_utextbox = self.driver.find_element(By.ID, "email").is_displayed()
        assert actual_utextbox == True

    def test_verifyUsername_textbox_typed_text(self):
        self.driver.find_element(By.ID, "email").send_keys("victor")
        actual_utextbox = self.driver.find_element(By.ID, "email").get_attribute("value")
        assert actual_utextbox == "victor"
