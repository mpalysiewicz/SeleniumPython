from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


def test_check_basket_quantity(web_driver: WebDriver):
    button_most_wanted = web_driver.find_element(By.XPATH, "//*[@id='menu-item-128']/a")
    button_most_wanted.click()
    time.sleep(2)
    button_ad_magnolia = web_driver.find_element(By.XPATH, "//*[@id='page']/div/div/div[2]/div/ul/li[2]/a[2]")
    button_ad_magnolia.click()
    time.sleep(2)
    my_card = web_driver.find_element(By.XPATH, '//*[@id="page"]/header[1]/div/div/div/ul/li[2]/a')
    my_card.click()
    time.sleep(2)
    wartosc_poczatkowa = web_driver.find_element(By.XPATH, "//div[@class='quantity']//input[@type='number']")
    wartosc_poczatkowa_value = wartosc_poczatkowa.get_attribute('value')
    wartosc_poczatkowa_int = int(wartosc_poczatkowa_value)
    plus = web_driver.find_element(By.XPATH, '//*[@id="post-6"]/div[2]/form/table/tbody/tr[1]/td[5]/div/div/a[2]')
    time.sleep(2) #proszę dodać WebDriver wait zamist time.sleep
    plus.click()
    time.sleep(1)
    plus.click()
    time.sleep(1)
    cart_update = web_driver.find_element(By.XPATH, '//*[@id="post-6"]/div[2]/form/table/tbody/tr[2]/td/input[1]').click()
    time.sleep(1)
    wartosc_koncowa = int(web_driver.find_element(By.XPATH, "//div[@class='quantity']//input[@type='number']").get_attribute('value'))
    time.sleep(1)
    assert wartosc_koncowa  != wartosc_poczatkowa_int, "Warning koszyk"