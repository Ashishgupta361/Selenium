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
expectedlist = ["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]
actualList = []
productslist = driver.find_elements(By.XPATH,"//h4[@class='product-name']")

for productname in productslist:
    print(productname.text)
    actualList.append(productname.text)

assert expectedlist == actualList










































