import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Get the absolute path to the HTML file
        file_path = os.path.abspath("Home.html")

        await page.goto(f"file://{file_path}")

        # Scroll to the literature section
        await page.evaluate("document.getElementById('literature').scrollIntoView()")

        # Wait for the animation to be visible
        await page.wait_for_timeout(2000) # Wait for 2 seconds for animation

        # Take a screenshot
        await page.screenshot(path="jules-scratch/verification/literature_animation.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())