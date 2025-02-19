import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.naukri.com/")
driver.find_element(By.LINK_TEXT,"Login").click()

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("ashishjhi361@gmail.com")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("#Naukari@12345")

driver.find_element(By.XPATH,"//button[@class='btn-primary loginButton']").click()

driver.find_element(By.XPATH,"//div[@class='nI-gNb-drawer__icon']").click()
driver.find_element(By.LINK_TEXT,"View & Update Profile").click()

driver.find_element(By.XPATH,"//div[@class='widgetHead']/span[@class='edit icon']").click()
# Try clearing the input field using the clear() method
try:
    driver.find_element(By.CSS_SELECTOR,"#resumeHeadlineTxt").clear()
except Exception as e:
    # If the clear() method fails, use JavaScript to clear the input field
    driver.execute_script("arguments[0].value = '';", driver.find_element(By.CSS_SELECTOR,"#resumeHeadlineTxt"))

driver.find_element(By.CSS_SELECTOR,"#resumeHeadlineTxt").send_keys("Software test engineer/ Automation tester")
driver.find_element(By.XPATH,"//div[@class='action s12']/button[@type='submit']").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='nI-gNb-drawer__icon']")))
driver.find_element(By.XPATH,"//div[@class='nI-gNb-drawer__icon']").click()
driver.find_element(By.XPATH,"//a[@title='Logout']").click()
time.sleep(5)