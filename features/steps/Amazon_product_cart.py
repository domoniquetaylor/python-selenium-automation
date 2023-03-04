from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button')
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
CART = (By.ID, 'nav-cart-count')



@when('Input text {text}')
def input_search_text(context, text):
    context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(text)


@when('Click on Search button')
def click_search_button(context):
    context.driver.find_element(*SEARCH_ICON).click()


@when('Click on a product')
def select_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@when('Click Add to Cart button')
def add_product_to_cart(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()


@when('Open Cart Page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')

@then('Verify that cart has {expected_number} item(s)')
def verify_item_cart(context, expected_number):
    actual_number = context.driver.find_element(*CART).text


    assert expected_number == actual_number, f'Expected {expected_number}, but got {actual_number}'