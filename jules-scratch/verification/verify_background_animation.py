from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("file:///app/Home.html")

    # Scroll down to trigger the animation
    page.evaluate("window.scrollTo(0, 500)")

    # Wait for animations to settle
    page.wait_for_timeout(1000)

    page.screenshot(path="jules-scratch/verification/verification.png")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)