import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_check_page_title():
    driver = webdriver.Chrome('/Users/miroslawpalysiewicz/Documents/Selenium/Webdriver/chromedriver')

    driver.get('http://skleptest.pl/')
    time.sleep(2) # Let the user actually see something!

    search_box = driver.find_element(By.ID, "search-field-top-bar")
    search_box.send_keys('Black top')
    search_box.submit()

    time.sleep(5)
    page_title = driver.find_element(By.XPATH, "//h1[@class='page-title']/span").text
    #assert page_title.lower() == "black top"
    assert page_title.casefold() == "black top"

    driver.quit()