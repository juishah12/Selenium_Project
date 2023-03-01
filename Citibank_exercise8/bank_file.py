import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.online.citibank.co.in/")
driver.find_element(By.CLASS_NAME, "fancybox-close").click()
driver.find_element(By.XPATH,"//span[normalize-space()='Login']").click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH,"//div[contains(text(),' Forgot User ID? ')]").click()

driver.find_element(By.LINK_TEXT,"select your product type").click()
driver.find_element(By.LINK_TEXT,"Credit Card").click()

driver.find_element(By.CSS_SELECTOR,"#citiCard1").send_keys("7897")
driver.find_element(By.CSS_SELECTOR,"input[name='citiCard2']").send_keys("7897")
driver.find_element(By.CSS_SELECTOR,"[name='citiCard3']").send_keys("7897")
driver.find_element(By.ID,"citiCard4").send_keys("7897")

driver.find_element(By.ID,"cvvnumber").send_keys("889")
driver.execute_script("document.querySelector('#bill-date-long').value='11/09/2000'")
