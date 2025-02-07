import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

assert driver.find_element(By.ID,"displayed-text").is_displayed()
time.sleep(2)
# Click on Hide button
driver.find_element(By.ID,"hide-textbox").click()
time.sleep(2)
assert driver.find_element(By.ID,"displayed-text").is_displayed(),"box is not displayed"
