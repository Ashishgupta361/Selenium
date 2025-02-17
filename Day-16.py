import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.naukri.com/")
driver.find_element(By.LINK_TEXT,"Login").click()

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("ashishjhi361@gmail.com")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("#Naukari@12345")

driver.find_element(By.XPATH,"//button[@class='btn-primary loginButton']").click()

driver.find_element(By.XPATH,"//div[@class='nI-gNb-drawer__icon']").click()
driver.find_element(By.LINK_TEXT,"View & Update Profile").click()
#driver.find_element(By.XPATH,"//a[@class='close']").click()
driver.find_element(By.XPATH,"//div[@xpath='1']/span[@tabindex='0']").click()
driver.find_element(By.XPATH,"//input[id='locationSugg']").click()
locationsChecked = driver.find_elements(By.XPATH,"//li[@class='sugTouple Checked']")
for location in locationsChecked:
    if location.text =="Bengaluru":
        location.find_element(By.XPATH,"i[@class='icon']").click()


locationsUnChecked = driver.find_elements(By.XPATH,"//li[@class='sugTouple UnChecked']")
for location in locationsUnChecked:
    if location.text =="Chennai":
        location.find_element(By.XPATH,"i[@class='icon']").click()

driver.find_element(By.ID,"saveDesiredProfile").click()
time.sleep(10)