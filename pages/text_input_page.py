from playwright.async_api import Page

class TextInputPage:
    def __init__(self, page: Page):
        self.page = page
        self.text_field = page.get_by_role("textbox")
        self.button = page.locator("#updatingButton")

    async def open(self):
        await self.page.goto("https://www.uitestingplayground.com/textinput")

    async def enter_text(self, text: str):
        await self.text_field.fill(text)

    async def click_button(self):
        await self.button.click()

    async def get_button_text(self):
        return await self.button.text_content()
