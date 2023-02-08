import time

from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webdriver import WebDriver


def test_check_page_title(web_driver: WebDriver):
    search_box = web_driver.find_element(By.ID, "search-field-top-bar")
    search_box.send_keys('Black top')
    search_box.submit()

    time.sleep(2)
    page_title = web_driver.find_element(By.XPATH, "//h1[@class='page-title']/span").text
    assert page_title.lower() == "black top"
