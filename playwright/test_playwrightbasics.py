import time

from playwright.sync_api import Page, expect, Playwright

'''
Explicitly declaring this, will make things easier for people to understand methods and trace 
'''

def test_playwright_basics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context() #do some operations, login ->
    page = context.new_page() # in case you want to perform a scenario without closing other one
    page.goto("https://www.youtube.com/watch?v=RjMbCUpvIgw&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=10")

#same above with a shortcut
#chromium headless mode, 1 single context. we can use this 90% of the time
def test_playwright_short_cut(page:Page):
    page.goto("https://www.youtube.com/watch?v=RjMbCUpvIgw&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=10")

'''
We can click on run button, use run configuration and provide additional configurations
'''

#id  .classname --> CSS Selector for the element
def test_core_locators(page:Page):
    page.goto("http://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learninggg")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link",name="terms and conditions")
    page.get_by_role("button",name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password")).to_be_visible()

    #Incorrect username/password  -  assertion
    time.sleep(5)
'''
if you are finding something by label, ensure there is a label tag. input is available, then we can provide input
or atleast use for attribute, if id id linked to for attribute
'''

def test_firefoxBrowser(playwright: Playwright):
    firefoxBrowser = playwright.firefox
    browser = firefoxBrowser.launch(headless= False)
    page = browser.new_page()
    page.goto("http://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions")
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password")).to_be_visible()