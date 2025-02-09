from selenium import webdriver
from selenium.webdriver.common.by import By
# name variable to store the name of user
name = "Ashish"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH,"//input[@name='enter-name']").send_keys(name)
driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
# switch_to is used to switch from current tab control to any pop-up/tab in browser
alert = driver.switch_to.alert
alertmessage = alert.text
print(alertmessage)
# click ok on alert box accept method is used
alert.accept()
# click cancel on alert box dismiss method is used
# alert.dismiss()
assert name in alertmessage,f"{name} not displayed in alert box"