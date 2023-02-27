import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://netbanking.hdfcbank.com/netbanking/")

driver.switch_to.frame(driver.find_element(By.XPATH,"//frame[@name='login_page']"))
driver.find_element(By.NAME,"fldLoginUserId").send_keys("test123")
driver.find_element(By.LINK_TEXT,"CONTINUE").click()
time.sleep(10)
#driver.find_element(By.XPATH, "//a[@class='btn btn-primary login-btn']").click()

