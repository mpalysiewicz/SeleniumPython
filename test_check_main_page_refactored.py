import string
import time
import my_account_page
from random import choice
from telnetlib import EC

from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


def test_check_page_title(web_driver: WebDriver):
    search_box = web_driver.find_element(By.ID, "search-field-top-bar")
    search_box.send_keys('Black top')
    search_box.submit()

    time.sleep(2)
    page_title = web_driver.find_element(By.XPATH, "//h1[@class='page-title']/span").text
    assert page_title.lower() == "black top"


def test_register_user(web_driver: WebDriver):
    user = "".join(choice(string.ascii_letters) for i in range(10)) + \
           "".join(choice(string.digits) for i in range(10))
    hello_message = my_account_page.register_user(web_driver, user)

    assert user in hello_message, \
        f"{user} does not present in {hello_message}"

def test_login_user(web_driver: WebDriver):
    user = "Mirek.Python"
    web_driver.find_element(By.XPATH, "//li[@class='top-account']").click()
    web_driver.find_element(By.XPATH, "//input[@id='username']").send_keys(user +"@gmail.com")
    web_driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Aut0m@ty$a$uper!")
    web_driver.find_element(By.XPATH, "//input[@name='login']").click()
    time.sleep(5)