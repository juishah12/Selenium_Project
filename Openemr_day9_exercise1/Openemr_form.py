from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://demo.openemr.io/b/openemr/")
driver.find_element(By.ID, "authUser").send_keys("admin")
driver.find_element(By.ID, "clearPass").send_keys("pass")
# Using XPath Directly
select_lang=Select(driver.find_element(By.XPATH,"//select[@name='languageChoice']"))
select_lang.select_by_visible_text("English (Indian)")

driver.find_element(By.CSS_SELECTOR,"#login-button").click()

# 6.	Click on Patient  Click New Search
driver.find_element(By.XPATH,"//div[text()='Patient']").click()
driver.find_element(By.XPATH,"//div[text()='New/Search']").click()

# 7.	Add the first name,
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@name='pat']"))
driver.find_element(By.ID,"form_fname").send_keys("john")
driver.find_element(By.XPATH,"//input[@id='form_lname']").send_keys("wick")

select_gender=Select(driver.find_element(By.XPATH,"//select[@id='form_sex']"))
select_gender.select_by_visible_text("Male")

driver.find_element(By.XPATH,"//input[@id='form_DOB']").send_keys("2023-03-01")

#click on create new patient
driver.find_element(By.XPATH,"//button[@id='create']").click()

driver.switch_to.default_content()

#click on Confirm Create New Patient
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='modalframe']"))
driver.find_element(By.XPATH,"//input[@value='Confirm Create New Patient']").click()
driver.switch_to.default_content()

#wait for alert is present
wait=WebDriverWait(driver,120)
wait.until(expected_conditions.alert_is_present())

actual_alert_text=driver.switch_to.alert.text
print(actual_alert_text)

driver.switch_to.alert.accept()

if len(driver.find_elements(By.XPATH,"//div[@class='closeDlgIframe']"))>0:
    driver.find_element(By.XPATH,"//div[@class='closeDlgIframe']").click()

driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@name='pat']"))

actual_added_patient=driver.find_element(By.XPATH,"//i[@class='fa fa-question-circle']/ancestor::h2").text
print(actual_added_patient)
time.sleep(5)
driver.quit()