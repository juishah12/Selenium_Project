import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")
driver.title
driver.implicitly_wait(30)


driver.find_element(By.NAME, "UserFirstName").send_keys( "kin")
driver.find_element(By.NAME, "UserLastName").send_keys("mike")
driver.find_element(By.NAME, "UserEmail").send_keys("kin@gmail.com")
driver.find_element(By.NAME, "UserTitle").click()
#driver.find_element(By.XPATH, "//select[@name='UserTitle']/option[text()='IT Manager']").click()
select_Jobtitle = Select(driver.find_element(By.NAME, "UserTitle"))
select_Jobtitle.select_by_value("Sales_Manager_AP")
# "//select[@name='element_name']/option[text()='option_text']").click()
driver.find_element(By.XPATH, "//select[@name='CompanyEmployees']/option[text()='101 - 500 employees']").click()
select_country=Select(driver.find_element(By.NAME,"CompanyCountry"))
select_country.select_by_value("US")
select_state=Select(driver.find_element(By.NAME,"CompanyState"))
select_state.select_by_value("AL")
driver.find_element(By.XPATH, "//div[@class='checkbox-ui']").click()
driver.find_element(By.NAME, "UserPhone").send_keys("9825040367")
driver.find_element(By.NAME,"CompanyName").send_keys("Arrow")
actual_error=driver.find_element(By.XPATH, "//span[contains(text(),'valid Phone')]").text
print(actual_error)
driver.find_element(By.NAME,"start my free trial").click()
#driver.find_element(By.XPATH, "//select[@name='CompanyCountry']/option[text()='United Kingdom']").click()    driver.implicitly_wait(10)    driver.find_element(By.XPATH, "//div[@class='checkbox-ui']").click()    driver.implicitly_wait(10)    driver.find_element(By.NAME, "start my free trial").click()
time.sleep(25)
driver.quit()