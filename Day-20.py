import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
mail = driver.find_element(By.XPATH,"//div/p[@class='im-para red']/strong").text

driver.switch_to.window(windowsOpened[0])

driver.find_element(By.ID,"username").send_keys(mail)
driver.find_element(By.ID,"password").send_keys("12345")
driver.find_element(By.ID,"terms").click()
driver.find_element(By.CSS_SELECTOR,"#signInBtn").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='alert alert-danger col-md-12']")))
message = driver.find_element(By.XPATH,"//div[@class='alert alert-danger col-md-12']").text
print(message)

time.sleep(5)