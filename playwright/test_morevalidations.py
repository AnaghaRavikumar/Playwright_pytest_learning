import time

from playwright.sync_api import Page, expect


def test_ui_checks(page:Page):

    #hide/display  and placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #AlertBoxes
    #We can create anonymous functions using lambda
    page.on("dialog",lambda dialog:dialog.accept())
    page.get_by_role("button",name="Confirm").click()
    time.sleep(5)

    #playwright codegen https://rahulshettyacademy.com/client  --> gives locators by recording the steps we perform

    #Mouse Hover
    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Top").click()

    #Frame Handle
    page_frame = page.frame_locator("#courses-iframe")
    page_frame.get_by_role("link", name= "All access plan").click()
    expect(page_frame.locator("body")).to_contain_text("Happy Subscibers")

    #Handling WebTables
    #check price of rice is equal to 37
    #identify the price column
    #identify the row
    #extract price of rice
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            price_col_value = index
            print(f"Price column value is {price_col_value}")
            break

    rice_row = page.locator("tr").filter(has_text = "Rice")
    expect(rice_row.locator("td").nth(price_col_value)).to_have_text("37")



