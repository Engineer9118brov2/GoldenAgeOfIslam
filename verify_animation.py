import asyncio
import os
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Get the absolute path to the HTML file
        file_path = os.path.abspath('Home.html')

        # Go to the local HTML file
        await page.goto(f'file://{file_path}', wait_until='networkidle')

        # Scroll to the literature section
        await page.evaluate('document.getElementById("literature").scrollIntoView()')

        # Wait for the animation to be visible
        await page.wait_for_timeout(4000)  # Wait 4 seconds for animation

        # Take a screenshot
        await page.screenshot(path='playwright_screenshots/literature_animation_delayed.png')

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())