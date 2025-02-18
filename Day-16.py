import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.naukri.com/")
driver.find_element(By.LINK_TEXT,"Login").click()

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("ashishjhi361@gmail.com")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("#Naukari@12345")

driver.find_element(By.XPATH,"//button[@class='btn-primary loginButton']").click()

driver.find_element(By.XPATH,"//div[@class='nI-gNb-drawer__icon']").click()
driver.find_element(By.LINK_TEXT,"View & Update Profile").click()

driver.execute_script("window.scrollTo(0,3000);")

editXpath = "//div[@class='desiredProfile']/div[@class='card']/div/div[@class='widgetHead']/span[@class='edit icon']"
editElement = driver.find_element(By.XPATH, editXpath)
editElement.click()

# Now you can interact with the element
driver.execute_script("window.scrollTo(0,500);")

driver.find_element(By.CSS_SELECTOR,"#locationSugg").click()

locationsChecked = driver.find_elements(By.XPATH,"//li[@class='sugTouple Checked']")
for location in locationsChecked:
    if location.text =="Bengaluru":
        location.find_element(By.XPATH,"i[@class='icon']").click()


locationsUnChecked = driver.find_elements(By.XPATH,"//li[@class='sugTouple UnChecked']")
for location in locationsUnChecked:
    if location.text =="Chennai":
        location.find_element(By.XPATH,"i[@class='icon']").click()

driver.find_element(By.ID,"saveDesiredProfile").click()
driver.find_element(By.XPATH,"//div[@class='nI-gNb-drawer__icon']").click()
driver.find_element(By.XPATH,"//a[@title='Logout']").click()
time.sleep(5)