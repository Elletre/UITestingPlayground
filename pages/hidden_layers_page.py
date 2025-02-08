from playwright.async_api import Page

class HiddenLayersPage:
    def __init__(self, page: Page):
        self.page = page
        self.green_button = page.locator("#greenButton")
        self.blue_button = page.locator("#blueButton")

    async def open(self):
        await self.page.goto("https://www.uitestingplayground.com/hiddenlayers")

    async def click_green_button(self):
        await self.green_button.click()

    async def is_blue_button_visible(self):
        return await self.blue_button.is_visible()