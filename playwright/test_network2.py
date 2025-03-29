import time

from playwright.sync_api import Page, Playwright, expect

from utils.api_base import APIUtils


#-> api call from browser, api call contacts server and returns response to browser -> browser uses this response to  generate html
#in case user is  not authorized to visit some  data, we can intercept the api call with other users data in url to mock the web page/software

def intercept_request(route):
    route.continue_("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae4c0b9f6fb")


def test_network_2(page: Page):
    page.goto("https://rahulshettyacademy.com/client")

    #tell palywright to start listening the network call, using *because it is id and keep changing for logins.
    #* would be a regEx that accepts any alphanumerics
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_placeholder("email@example.com").fill("aghirm@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("12345678")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()

    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)


def test_session_storage(playwright: Playwright):
    api_utils = APIUtils()
    get_token = api_utils.get_token(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #script to inject token in session local storage
    page.add_init_script(f"""localStorage.setItem('token','{get_token}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text('Your Orders')).to_be_visible()
