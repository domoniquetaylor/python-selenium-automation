from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(executable_path='C:\\Users\\domon\\OneDrive\\Desktop\\QA Automation GitHub\\python-selenium-automation\\chromedriver.exe')
service = Service('C:\\Users\\domon\\OneDrive\\Desktop\\QA Automation GitHub\\python-selenium-automation\\chromedriver.exe')
driver = webdriver.Chrome(service=service)



# Part 1 of Homework

# Amazon Logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo'])

# Continue button
driver.find_element(By.ID, 'continue' )

# Need Help Link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Forgot password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

# Other issues with sign in link
driver.find_element(By.ID, 'ap-other-signin-issues-link')

# Create account button
driver.find_element(By.ID, 'createAccountSubmit')

# Conditions of use link
driver.find_element(By.XPATH, "//a[contains(@href,'ref=ap_signin_notification_condition_of_use')]")

# Privacy Notice button
driver.find_element(By.XPATH, "//a[contains(@href,'ref=ap_signin_notification_privacy_notice')]")






