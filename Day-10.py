import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
time.sleep(2)
products = driver.find_elements(By.XPATH,"//div[@class='product']")

print(len(products))

for product in products:
    product.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()

driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

prices = driver.find_elements(By.XPATH,"//td[5]/p[@class='amount']")
sum = 0
for price in prices:
    sum = sum + int(price.text)

totalAmount = driver.find_element(By.CSS_SELECTOR,".totAmt").text
# Assert sum of individual item value is equal to total amount
if sum == int(totalAmount):
    print("sum of individual item value is equal to total amount")

assert sum == int(totalAmount)

# Assert whether total amount is greater than or equal to total amount after discount
discountedtotalAmount = driver.find_element(By.CSS_SELECTOR,".discountAmt")
if int(totalAmount) >= int(discountedtotalAmount.text):
    print("total amount is greater than or equal to total amount after discount")

assert int(totalAmount) >= int(discountedtotalAmount.text)


driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulsheetyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
# Explicit wait
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))

message = driver.find_element(By.CSS_SELECTOR,".promoInfo").text
print(message)


time.sleep(3)