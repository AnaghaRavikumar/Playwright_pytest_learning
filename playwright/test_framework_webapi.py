import json

import pytest
from playwright.sync_api import Playwright, expect

from utils.api_base import APIUtils

# Json file -> utility to convert it to dictionary ->  access it into test
with open('data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']

#parameterize, it will check th dataset in json, every run it will pick up one data and run for it.This way
#we can test for multiple data set in the same method
@pytest.mark.parametrize('user_credentials',user_credentials_list)
def test_e2e_web_api(playwright:Playwright, user_credentials):
    browser = playwright.chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()


    #create order --> order_id
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright)

    #login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill(user_credentials["user_email"])
    page.get_by_placeholder("enter your passsword").fill(user_credentials["user_password"])
    page.get_by_role("button",name="Login").click()

    page.get_by_role("button",name="ORDERS").click()


    #orders History page -> order is present.
    row = page.locator("tr").filter(has_text =order_id)
    row.get_by_role("button",name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()