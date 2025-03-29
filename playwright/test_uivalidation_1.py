import time

from playwright.sync_api import Page, expect


def test_ui_validation_dynamic_script(page:Page):
    #iphone X,  Nokia Edge -> verify 2 items are showing in cart
    page.goto("http://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions")
    page.get_by_role("button", name="Sign In").click()
    #there are som custom components dev made, we use locator
    iphone_product = page.locator("app-card").filter(has_text="iphone X")
    iphone_product.get_by_role("button").click()
    nokia_product = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_product.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

def test_child_wiindow_handle(page:Page):
    page.goto("http://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newPage_info: #we are giving python closure, triggering an event
        #step1
        #step2
        page.locator(".blinkingText").click() #new page
        child_page= newPage_info.value
        text = child_page.locator(".red").text_content()
        print(text)
        words = text.split("at")
        email = words[1].strip().split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"











