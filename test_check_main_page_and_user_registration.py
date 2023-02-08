import string
import time
from random import choice
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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
    web_driver.find_element(By.XPATH, "//li[@class='top-account']").click()
    web_driver.find_element(By.XPATH, "//input[@id='reg_email']").send_keys(user + "@gmail.com")
    web_driver.find_element(By.XPATH, "//input[@id='reg_password']").send_keys(
        user.join(choice(string.punctuation) for i in range(10)))
    web_driver.find_element(By.XPATH, "//h2[contains(text(),'Register')]").click()
    WebDriverWait(web_driver, 30).until(EC.element_to_be_clickable(By.XPATH, "//input[@class='woocommerce-Button button' and @name='register']"))
    web_driver.find_element(By.XPATH, "//input[@class='woocommerce-Button button' and @name='register']").click()
    WebDriverWait(web_driver, 30).until(
        EC.presence_of_element_located(By.XPATH, "//div[@class='woocommerce-MyAccount-content']"))
    hello_message = web_driver.find_element(By.XPATH, "//div[@class='woocommerce-MyAccount-content']").text
    assert user in hello_message, \
        f"{user} does not present in {hello_message}"

def test_login_user(web_driver: WebDriver):
    user = "Mirek.Python"
    web_driver.find_element(By.XPATH, "//li[@class='top-account']").click()
    web_driver.find_element(By.XPATH, "//input[@id='username']").send_keys(user +"@gmail.com")
    web_driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Aut0m@ty$a$uper!")
    web_driver.find_element(By.XPATH, "//input[@name='login']").click()
    time.sleep(5)