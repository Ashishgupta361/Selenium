from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
# window handles returns list of opened tabs/windows in current browser
windowsopened = driver.window_handles

driver.switch_to.window(windowsopened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)

driver.switch_to.window(windowsopened[0])
print(driver.find_element(By.TAG_NAME,"h3").text)
