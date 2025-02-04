import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("ind")
# added time.sleep because it takes time to load the suggestions
time.sleep(2)
# Auto suggestive drop-down
# find+elements returns list of web elements
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break

time.sleep(3)

# .text will not return the value generated dynamically
# e.g.-> print(driver.find_element(By.ID,"autosuggest").text) will not return any value

# get_attribute("value") will return the dynamic value
print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))

assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"