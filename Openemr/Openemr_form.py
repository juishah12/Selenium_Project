from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://demo.openemr.io/b/openemr/")
driver.find_element(By.ID, "authUser").send_keys("admin")
driver.find_element(By.ID, "clearPass").send_keys("pass")
# Using XPath Directly
driver.find_element(By.XPATH, "//option[contains(@value,'18')]").click()
select_lang = Select(driver.find_element(By.XPATH, "//select[@name='languageChoice']"))select_lang.select_by_visible_text("English (Indian)")
driver.find_element(By.ID, "login-button").click()