from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file://{os.getcwd()}/Home.html")

        # Scroll to each section and take a screenshot
        page.evaluate("document.getElementById('medicine').scrollIntoView()")
        page.wait_for_timeout(1000) # wait for animation
        page.screenshot(path="jules-scratch/verification/medicine.png")

        page.evaluate("document.getElementById('mathematics').scrollIntoView()")
        page.wait_for_timeout(1000) # wait for animation
        page.screenshot(path="jules-scratch/verification/mathematics.png")

        page.evaluate("document.getElementById('literature').scrollIntoView()")
        page.wait_for_timeout(1000) # wait for animation
        page.screenshot(path="jules-scratch/verification/literature.png")

        browser.close()

if __name__ == "__main__":
    import os
    run()