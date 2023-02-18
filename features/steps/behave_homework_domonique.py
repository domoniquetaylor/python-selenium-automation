from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click Orders')
def click_orders_button(context):
    context.driver.find_element(By.XPATH, "//span[text()='& Orders']").click()


@then('Sign In header is visible')
def sign_in_header(context):
    context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")


@then('Email input field is present')
def email_input_field(context):
    context.driver.find_element(By.ID, "ap_email")



@when('Click Cart Icon')
def shopping_cart_icon(context):
    context.driver.find_element(By.XPATH, "//span[@class='nav-cart-icon nav-sprite']").click()


@then('Verify Cart is Empty')
def empty_amazon_cart(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//h2[contains(text(),'Your Amazon Cart is empty')]").text


    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'

