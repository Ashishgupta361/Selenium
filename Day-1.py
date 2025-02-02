# Import the webdriver package
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
# Locators => ID, Xpath, CSS Selector, Classname , linkText
driver.find_element(By.NAME,"name").send_keys("Ashish")
driver.find_element(By.NAME,"email").send_keys("as@gmial.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345")
driver.find_element(By.CSS_SELECTOR,"#exampleCheck1").click()


#driver.close()