import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"name").send_keys("Ashish")
driver.find_element(By.NAME,"email").send_keys("as@gmial.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345")
driver.find_element(By.CSS_SELECTOR,"#exampleCheck1").click()
# Xpath => //tagname[@attribute='value']
# Static drop down using Select class
dropdown = Select(driver.find_element(By.CSS_SELECTOR,"select[id='exampleFormControlSelect1']"))
dropdown.select_by_visible_text("Male")
driver.find_element(By.XPATH,"//input[@id='inlineRadio1']").click()
driver.find_element(By.XPATH,"//input[@name='bday']").send_keys("03-02-2025")
# CSS Selector => tagname[attribute='value']
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
time.sleep(2)