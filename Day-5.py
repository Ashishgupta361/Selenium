import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# Dynamically handling radio buttton
# find_elements returns list of web elements
radiobuttons = driver.find_elements(By.XPATH,"//input[@name='radioButton']")

print(len(radiobuttons))

for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio1":
        radiobutton.click()
        assert radiobutton.is_selected()
        break

time.sleep(3)