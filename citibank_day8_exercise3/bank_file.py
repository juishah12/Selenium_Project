import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.online.citibank.co.in/")
#driver.find_element(By.CLASS_NAME, "fancybox-close").click()
driver.find_element(By.XPATH,"//span[normalize-space()='Login']").click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.XPATH,"//div[contains(text(),' Forgot User ID? ')]").click()
driver.find_element(By.LINK_TEXT,"select your product type").click()
driver.find_element(By.LINK_TEXT,"Credit Card").click()

driver.find_element(By.CSS_SELECTOR,"#citiCard1").send_keys("7897")
driver.find_element(By.CSS_SELECTOR,"input[name='citiCard2']").send_keys("7897")
driver.find_element(By.CSS_SELECTOR,"[name='citiCard3']").send_keys("7897")
driver.find_element(By.ID,"citiCard4").send_keys("7897")

driver.find_element(By.ID,"cvvnumber").send_keys("889")
# driver.execute_script("document.querySelector('#bill-date-long').value='11/09/2000'")
# driver.find_element(By.XPATH, "//input[@value='PROCEED']").click()
driver.find_element(By.ID,"bill-date-long").click()
select_year= Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
select_year.select_by_value("2022")
select_month= Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
select_month.select_by_value("3")
driver.find_element(By.LINK_TEXT,"14").click()
# Approach 2
# driver.execute_script("document.querySelector('#bill-date-long').value='11/09/2001'")

# ele1 =driver.find_element(By.XPATH,"//input[@name='DOB']")
# driver.execute_script("arguments[0].value='11/09/2000'",ele1)
driver.find_element(By.XPATH,"//input[@type='button']").click()
time.sleep(3)
error_message = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/li").text
print(error_message)

