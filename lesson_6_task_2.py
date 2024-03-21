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

driver.get('http://uitestingplayground.com/textinput')
input = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input.clear()
input.send_keys('SkyPro')

button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')
button.click()
print(button.text)