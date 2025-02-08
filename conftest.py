import pytest
import pytest_asyncio
from playwright.async_api import async_playwright, Page


@pytest_asyncio.fixture(scope="function")
async def browser():
    """Creates a new browser instance for each test."""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # Change to False if no need to see browser instance
        yield browser
        await browser.close()


@pytest_asyncio.fixture(scope="function")
async def page(browser) -> Page:
    """Creates a new page instance for each test."""
    context = await browser.new_context(ignore_https_errors=True)
    page = await context.new_page()
    yield page
    await page.close()
    await context.close()
