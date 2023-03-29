import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://www.phptravels.net/home")
#
# driver.find_element(By.XPATH, "//a[normalize-space()='flights']").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//input[@id='autocomplete']").send_keys("LAX - Los Angeles Intl - Los Angeles")
# driver.find_element(By.XPATH, "//input[@id='autocomplete2']").send_keys("DAL - Dallas Love Fld - Dallas")
# time.sleep(2)
# driver.find_element(By.XPATH, "//div[@class='row g-0']//input[@id='departure']").clear()
# driver.find_element(By.XPATH, "(//input[@id='departure'])[1]").send_keys("2023-03-13")
# time.sleep(2)
# driver.find_element(By.XPATH, "//a[@role='button']").click()
# driver.find_element(By.XPATH, "//div[@class='dropdown-item adult_qty']//i[@class='la la-plus']").click()
# driver.find_element(By.XPATH, "//span[@class='ladda-label']//*[name()='svg']").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "(//img[@alt='no results'])[1]").is_displayed()
# driver.quit()

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.malaysiaairlines.com/my/en.html")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://phptravels.net/")
driver.implicitly_wait(5)

#driver.find_element(By.LINK_TEXT, 'Flights').click()

driver.find_element(By.NAME, 'from').send_keys('Los Angeles')
driver.find_element(By.XPATH, '//div[@class="autocomplete-result"]//b[contains(text(), "LAX")]').click()

driver.find_element(By.NAME, 'to').send_keys('Dallas')
driver.find_element(By.XPATH, '//div[@class="autocomplete-result"]//b[contains(text(), "DAL")]').click()

driver.find_element(By.ID, 'departure').clear()
driver.find_element(By.ID, 'departure').send_keys('30-03-2023')

driver.find_element(By.XPATH, '//label[contains(text(), "Passengers")]/..//a').click()
driver.find_element(By.XPATH, '//div[@class="dropdown-item adult_qty"]//div[@class="qtyInc"]/i').click()
print('Total adults => ', driver.find_element(By.ID, 'fadults').get_attribute('value'))

driver.find_element(By.ID, 'flights-search').click()

print('Flight Departure time => ',
      driver.find_element(By.XPATH, '(//p[@class="theme-search-results-item-flight-section-meta-time"])[1]').text)
print('Flight Destination time => ',
      driver.find_element(By.XPATH, '(//p[@class="theme-search-results-item-flight-section-meta-time"])[2]').text)

print('Flight departure city => ',
      driver.find_element(By.XPATH, '(//p[@class="theme-search-results-item-flight-section-meta-city"])[1]').text)
print('Flight destination city => ',
      driver.find_element(By.XPATH, '(//p[@class="theme-search-results-item-flight-section-meta-city"])[2]').text)

print('Flight date => ',
      driver.find_element(By.XPATH, '(//p[@class="theme-search-results-item-flight-section-meta-date"])[1]').text)

print('Flight duration => ',
      driver.find_element(By.XPATH, '(//div[@class="theme-search-results-item-flight-section-path-fly-time"])[1]').text)

print('Flight cost => ', driver.find_element(By.XPATH, '(//button/strong)[1]').text)

time.sleep(3)
driver.quit()