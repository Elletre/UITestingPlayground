from playwright.async_api import Page

class ClassAttributePage:
    def __init__(self, page: Page):
        self.page = page
        self.button = page.locator(".btn-primary")

    async def open(self):
        await self.page.goto("https://www.uitestingplayground.com/classattr")

    async def click_button(self):
        await self.button.click()

    async def is_button_visible(self):
        return await self.button.is_visible()