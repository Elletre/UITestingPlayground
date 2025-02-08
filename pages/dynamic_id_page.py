from playwright.async_api import Page

class DynamicIDPage:
    def __init__(self, page: Page):
        self.page = page
        self.button = page.locator("button:text('Button with Dynamic ID')")

    async def open(self):
        await self.page.goto("https://www.uitestingplayground.com/dynamicid")

    async def click_button(self):
        await self.button.click()

    async def is_button_visible(self):
        return await self.button.is_visible()