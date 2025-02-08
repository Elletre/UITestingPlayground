from playwright.async_api import Page

class LoadDelayPage:
    def __init__(self, page: Page):
        self.page = page
        self.button = page.get_by_role("button", name="Button Appearing After Delay")

    async def open(self):
        await self.page.goto("https://www.uitestingplayground.com/loaddelay")

    async def wait_for_button(self):
        await self.button.wait_for(state="visible", timeout=10000)
        return await self.button.is_visible()
