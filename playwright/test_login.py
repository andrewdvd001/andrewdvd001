import pytest
from playwright.sync_api import Page, expect

def test_successful_login(page: Page):
    # Open login page
    page.goto("https://opensource-demo.orangehrmlive.com/")

    # Fill login form
    page.fill('input[name="username"]', 'Admin')
    page.fill('input[name="password"]', 'admin123')
    page.click('button[type="submit"]')

    # Assert dashboard appears (auto-waits)
    expect(page.locator("h6")).to_have_text("Dashboard")

    # (Optional) take screenshot of success
    page.screenshot(path="login_success.png")
    
def test_failed_login(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/")
    page.fill('input[name="username"]', 'Admin')
    page.fill('input[name="password"]', 'wrongpassword')
    page.click('button[type="submit"]')

    # Assert error message appears (auto-waits)
    expect(page.locator(".oxd-alert-content")).to_have_text("Invalid credentials")

    # (Optional) take screenshot of failure
    page.screenshot(path="login_failure.png")