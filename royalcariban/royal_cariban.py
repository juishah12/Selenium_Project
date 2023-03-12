import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get("https://www.royalcaribbean.com")
driver.implicitly_wait(30)
#driver.find_element(By.XPATH,"//a[contains(@id='rciHeaderSignIn')]").click()
driver.find_element(By.CLASS_NAME,"headerSignIn__link").click()
driver.find_element(By.CLASS_NAME,"login__create-account").click()
driver.find_element(By.ID,"mat-input-3").send_keys("DENNIS")
driver.find_element(By.ID,"mat-input-4").send_keys("RICH")
#driver.find_element(By.)
driver.find_element(By.XPATH,"//mat-select[@id='mat-select-0']").click()
driver.find_element(By.XPATH,//input())
select_month=Select(driver.find_element(By.XPATH,"//span[@class='mat-option-text']"))
select_month.select_by_visible_text(' April ')
#Select(driver.find_element(By.XPATH,"//div[@role='listbox']")).select_by_value(' April ')
driver.find_element(By.XPATH,"//mat-select[@id='mat-select-2']").click()
Select(driver.find_element(By.XPATH,"//div[@role='listbox']")).select_by_value('4')
#Select(driver.find_element(By.XPATH, "//select[@class='mat-select-min-line']")).select_by_visible_text('7')
#
# driver.find_element(By.LINK_TEXT, "14").click()
time.sleep(30)