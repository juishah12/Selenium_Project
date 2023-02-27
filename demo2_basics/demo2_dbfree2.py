import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.goole.com")
token = driver.title
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.PARTIAL_LINK_TEXT,"phpmyAdmin")
driver.implicitly_wait(30)