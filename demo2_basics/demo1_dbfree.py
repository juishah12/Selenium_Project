import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.db4free.net/")
driver.title
driver.implicitly_wait(30)

driver.find_element(By.PARTIAL_LINK_TEXT,"phpMyAdmin ").click()
print(driver.window_handles)
print(driver.window_handles[0])
print(driver.window_handles[1])
driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(30)
driver.find_element(By.ID,"input_username").send_keys("bala")
driver.find_element(By.ID,"input_password").send_keys("Welcome123")
driver.find_element(By.ID, "input_go").click()
time.sleep(30)
driver.close()
