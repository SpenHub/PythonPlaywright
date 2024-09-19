import re
from playwright.sync_api import Page, expect


# def test_has_title(page: Page):
#     page.goto("https://playwright.dev/")

#     # Expect a title "to contain" a substring.
#     expect(page).to_have_title(re.compile("Playwright"))


# def test_get_started_link(page: Page):
#     page.goto("https://playwright.dev/")

#     # Click the get started link.
#     page.get_by_role("link", name="Get started").click()

#     # Expects page to have a heading with the name of Installation.
#     expect(page.get_by_role("heading", name="Installation")).to_be_visible()


# def test_CAPTCHA_validation_required(page: Page):
#     page.goto("https://lastcallmedia.com/contact")


def test_CAPTCHA_validation_required(page: Page):
    page.goto("https://lastcallmedia.com/contact")
    page.get_by_label("Name").click()
    page.get_by_label("Name").fill("Name")

    page.locator("#edit-mail").click()
    page.locator("#edit-mail").fill("email@email.com")

    page.get_by_label("Message").click()
    page.get_by_label("Message").fill("Message")

    page.get_by_role("button", name="Send", exact=True).click()
    expect(page.get_by_label("Error message")).to_be_visible()