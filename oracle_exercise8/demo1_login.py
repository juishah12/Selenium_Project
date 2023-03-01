import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Edge()
driver.get("https://www.oracle.com/in/database/")
driver.implicitly_wait(30)
driver.find_element(By.ID,"acctBtnLabel").click()
driver.find_element(By.XPATH,"//a[@class='u30darkcta']").click()
time.sleep(5)

title_page = driver.title
print("title pf page" , title_page)
url_page = driver.current_url
print("current URL of page " ,url_page)


driver.find_element(By.XPATH,"//input[@id='sso_username']").send_keys("John")
driver.find_element(By.XPATH,"//input[@id='ssopassword']").send_keys("Pass")
driver.find_element(By.ID,"signin_button").click()
error_message = driver.find_element(By.XPATH,"//div[contains(text(),'Invalid')]").text
print("error found is", error_message)
time.sleep(30)
driver.quit()