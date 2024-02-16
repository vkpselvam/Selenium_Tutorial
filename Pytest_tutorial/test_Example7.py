import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='class')
def init_chrome_driver(request):
    s1 = Service(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=s1)
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


@pytest.mark.usefixtures("init_chrome_driver")
class Base_chrome_Test:
    pass


class Test_FB_chrome(Base_chrome_Test):
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
