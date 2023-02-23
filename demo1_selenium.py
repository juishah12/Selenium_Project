import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.title
print(driver.title)

#driver.find_element(By.ID,"email").send_keys("jui12@yahoo.ca")
#driver.find_element(By.ID,"pass").send_keys("flower593")
#driver.find_element(By.NAME,"login").click()

#click on create new account
#enter first name john
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.LINK_TEXT,"Create new account").click()
driver.find_element(By.NAME,"firstname").send_keys("John")
driver.find_element(By.NAME,"lastname").send_keys("marry")
driver.find_element(By.ID,"password_step_input").send_keys("ABCdef123!")
driver.find_element(By.NAME,"reg_email__").send_keys("abc@gmail.com")
driver.find_element(By.XPATH,"//input[@value='1']").click()
driver.find_element(By.NAME,"websubmit").click()
time.sleep(10)
#print the title of the page.

