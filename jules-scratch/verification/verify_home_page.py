import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Get the absolute path to the HTML file
        import os
        file_path = os.path.abspath("Home.html")

        await page.goto(f"file://{file_path}")

        # Scroll through the page to trigger animations
        for i in range(5):
            await page.mouse.wheel(0, 1500)
            await page.wait_for_timeout(500)

        # Take a full-page screenshot
        await page.screenshot(path="jules-scratch/verification/verification.png", full_page=True)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())