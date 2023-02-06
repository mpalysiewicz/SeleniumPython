import time
import conftest


from selenium.webdriver.common.by import By

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def web_driver() -> WebDriver:
    firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    firefox_driver.maximize_window()
    firefox_driver.implicitly_wait(conftest.Constants.IMPLICITLY_WAIT)
    firefox_driver.get(conftest.Constants.MAIN_URL)
    yield firefox_driver
    firefox_driver.quit()


def test_check_page_title(web_driver: WebDriver):
    search_box = web_driver.find_element(By.ID, "search-field-top-bar")
    search_box.send_keys('Black top')
    search_box.submit()

    time.sleep(2)
    page_title = web_driver.find_element(By.XPATH, "//h1[@class='page-title']/span").text
    assert page_title.lower() == "black top"
