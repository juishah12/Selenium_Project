import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.implicitly_wait(30)
driver.get("https://www.online.citibank.co.in/")

element = driver.find_element(By.XPATH,"//a")
print(len(element))
text = element[0].text
print(text)
time.sleep(5)
driver.find_element(By.XPATH,"//a[@title=''").click()
