from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(executable_path='C:\\Users\\domon\\OneDrive\\Desktop\\QA Automation GitHub\\python-selenium-automation\\chromedriver.exe')
service = Service('C:\\Users\\domon\\OneDrive\\Desktop\\QA Automation GitHub\\python-selenium-automation\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')

# Logo
driver.find_element(By.CSS_SELECTOR,'i.a-icon-logo')

# Create Account
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# Your Name
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

# Mobile Number or Email
driver.find_element(By.CSS_SELECTOR, "input[type='email']")

# Password
driver.element(By.CSS_SELECTOR, '.auth-require-password-validation')

# Password must be at least 6 characters
driver.find_element(By.CSS_SELECTOR, 'div[class="a-alert-content"]')

# Re-enter Password
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

#Create your Amazon Account button
driver.find_element(By.CSS_SELECTOR, '.a-button-input')

#Conditions of Use
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")

#Privacy Notice
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")

#Sign in hyperlink
driver.find_element(By.CSS_SELECTOR, "a[href*='/ap/signin']" )

