from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(executable_path='C:\\Users\\domon\\OneDrive\\Desktop\\QA Automation GitHub\\python-selenium-automation\\chromedriver.exe')
service = Service('C:\\Users\\domon\\OneDrive\\Desktop\\QA Automation GitHub\\python-selenium-automation\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')

sleep(2)

driver.find_element(By.XPATH, "//span[text()='& Orders']").click()


expected_result = 'Create your Amazon account'
actual_result = driver.find_element(By.ID, 'createAccountSubmit').text
print(actual_result)

assert expected_result == actual_result
print('test passed')

driver.quit()