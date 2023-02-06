import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('/Users/miroslawpalysiewicz/Documents/Selenium/Webdriver/chromedriver')

driver.get('http://skleptest.pl/')

time.sleep(5)

search_box = driver.find_element(By.ID, "search-field-top-bar")
search_box.send_keys('Black top')

search_box.submit()

time.sleep(5)

driver.quit()