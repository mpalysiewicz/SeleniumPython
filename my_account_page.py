import string
import time
from random import choice
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Constant:
    ACCOUNT_BUTTON = (By.XPATH, "//li[@class='top-account']")
    REG_BUTTON = (By.XPATH, "//input[@class='woocommerce-Button button' and @name='register']")
    HELLO_MESSAGE = (By.XPATH, "//div[@class='woocommerce-MyAccount-content']")

def register_user(web_driver, user):
    web_driver.find_element(*Constant.ACCOUNT_BUTTON).click()
    web_driver.find_element(By.XPATH, "//input[@id='reg_email']").send_keys(user + "@gmail.com")
    web_driver.find_element(By.XPATH, "//input[@id='reg_password']").send_keys(
        user.join(choice(string.punctuation) for i in range(10)))
    web_driver.find_element(By.XPATH, "//h2[contains(text(),'Register')]").click()
    WebDriverWait(web_driver, 30).until(EC.element_to_be_clickable(Constant.REG_BUTTON))
    web_driver.find_element(*Constant.REG_BUTTON).click()
    WebDriverWait(web_driver, 30).until(EC.presence_of_element_located(Constant.HELLO_MESSAGE))
    hello_message = web_driver.find_element(*Constant.HELLO_MESSAGE).text
    return hello_message