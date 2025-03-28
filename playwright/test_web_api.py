from playwright.sync_api import Playwright, expect

from utils.api_base import APIUtils


def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()

    #create order --> order_id
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright)

    #login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("aghirm@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("12345678")
    page.get_by_role("button",name="Login").click()

    page.get_by_role("button",name="ORDERS").click()


    #orders History page -> order is present.
    row = page.locator("tr").filter(has_text =order_id)
    row.get_by_role("button",name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()