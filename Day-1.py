# Import the webdriver package
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
# Locators => ID, Xpath, CSS Selector, Classname , linkText
driver.find_element(By.NAME,"name").send_keys("Ashish")
driver.find_element(By.NAME,"email").send_keys("as@gmial.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345")
driver.find_element(By.CSS_SELECTOR,"#exampleCheck1").click()
# Xpath => //tagname[@attribute='value']
driver.find_element(By.XPATH,"//input[@id='inlineRadio1']").click()
driver.find_element(By.XPATH,"//input[@name='bday']").send_keys("03-02-2025")
# CSS Selector => tagname[attribute='value']
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
success_message = driver.find_element(By.CLASS_NAME,"alert-dismissible").text
print(success_message)
time.sleep(3)

#driver.close()