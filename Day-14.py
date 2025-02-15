import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.switch_to.frame("courses-iframe")
print(driver.find_element(By.XPATH,"//h2/span/strong").text)

driver.switch_to.default_content()
print(driver.find_element(By.XPATH,"//div[@class='block large-row-spacer']/fieldset/legend").text)