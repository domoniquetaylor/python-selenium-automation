from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@when('Click on Bestsellers link')
def click_bestsellers_link(context):
    context.driver.find_element(By.XPATH, "//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']").click()


@then('Verify links are visible')
def verify_links_visible(context):
    context.driver.find_element(By.ID, 'zg_header a')