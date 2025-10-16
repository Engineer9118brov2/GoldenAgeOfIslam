import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(record_video_dir="jules-scratch/verification/")

        # Navigate to the local HTML file
        await page.goto(f"file://{os.path.abspath('Home.html')}")

        # Wait for the page to load
        await page.wait_for_load_state('networkidle')

        # Scroll down to trigger the animations
        await page.evaluate('window.scrollBy(0, 500)')
        await asyncio.sleep(1)
        await page.evaluate('window.scrollBy(0, 500)')
        await asyncio.sleep(1)
        await page.evaluate('window.scrollBy(0, 500)')
        await asyncio.sleep(1)

        # Hover over the cards to show the 3D effect
        await page.hover('#medicine .achievement-card')
        await asyncio.sleep(1)
        await page.hover('#mathematics .achievement-card')
        await asyncio.sleep(1)
        await page.hover('#literature .achievement-card')
        await asyncio.sleep(1)

        await browser.close()

if __name__ == "__main__":
    import os
    asyncio.run(main())