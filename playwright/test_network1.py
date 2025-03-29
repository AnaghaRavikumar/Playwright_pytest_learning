
from playwright.sync_api import Page

fake_payload = {"data":[],"message":"No Orders"}
#-> api call from browser, api call contacts server and returns response to browser -> browser uses this response to  generate html

def intercept_response(route):
    route.fulfill(
        json = fake_payload
    )

def test_network1(page:Page):
    page.goto("https://rahulshettyacademy.com/client")

    #tell palywright to start listening the network call, using *because it is id and keep changing for logins.
    #* would be a regEx that accepts any alphanumerics
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("aghirm@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("12345678")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)