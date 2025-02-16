import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT,"Shop").click()
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for product in products:
    if product.find_element(By.XPATH,"div/h4").text == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()

driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()

driver.find_element(By.CSS_SELECTOR,"button[class='btn btn-success']").click()

driver.find_element(By.CSS_SELECTOR,"#country").send_keys("ind")
# explicit wait
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()

driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()

message = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
print(message)

if "Success" in message:
    print("Assertion is passed")
else:
    print("Fail")

assert "Success" in message
