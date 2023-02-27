import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://netbanking.hdfcbank.com/netbanking/IpinResetUsingOTP.htm")
driver.find_element(By.XPATH,"//img[@alt='Go']").click()
actual_alert_text = driver.switch_to.alert.text
print(actual_alert_text)
driver.switch_to.alert.accept()

time.sleep(10)
driver.quit()
