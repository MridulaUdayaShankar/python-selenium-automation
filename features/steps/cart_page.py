from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main_page(context):
    context.driver.get("https://www.target.com")


CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify cart empty message is shown')
def verify_cart_empty(context):
    expected_text='Your cart is empty'
    # actual_text= context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1").text
    # assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'
    context.app.cart_page.verify_cart_empty()


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    print(f'Actual product in cart name: {actual_name}')
    #assert "Traditional Medicinals Organic Chamomile with Lavender Herbal Tea - 16ct" in actual_name, f"Expected {"Traditional Medicinals Organic Chamomile with Lavender Herbal Tea - 16ct"} but got {actual_name}"
    # assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"
    # context.app.cart_page.verify_product_name(context.app.search_results_page.get_product_name())
    context.app.cart_page.verify_product_name(context.product_name)

@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    # assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"
    context.app.cart_page.verify_cart_items(amount)