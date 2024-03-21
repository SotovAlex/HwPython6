from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)

driver.get('http://uitestingplayground.com/ajax')
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.bg-success')))
print(driver.find_element(By.CSS_SELECTOR, '.bg-success').text)