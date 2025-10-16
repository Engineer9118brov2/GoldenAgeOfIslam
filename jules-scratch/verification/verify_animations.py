import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Navigate to the local HTML file
        await page.goto(f"file://{os.path.abspath('Home.html')}")

        # Disable animations to ensure consistent screenshots
        await page.evaluate("""() => {
            const style = document.createElement('style');
            style.innerHTML = `
                *, *::before, *::after {
                    transition-duration: 0s !important;
                    animation-duration: 0s !important;
                    animation-delay: 0s !important;
                    scroll-behavior: auto !important;
                }
            `;
            document.head.appendChild(style);
        }""")

        # Wait for the page to load and elements to be visible
        await page.wait_for_selector('.achievement-card', timeout=5000)

        # Take a full-page screenshot
        await page.screenshot(path="jules-scratch/verification/verification.png", full_page=True)

        await browser.close()

if __name__ == "__main__":
    import os
    asyncio.run(main())