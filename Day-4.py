import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# Handling checkboxes dynamically
# Create list of all checkboxes
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

print(len(checkboxes))
# Iterate through the list of checkboxes and click on desired checkbox
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        # Checking if checkbox is clicked or not using is_selected()
        assert checkbox.is_selected()
        break

time.sleep(5)