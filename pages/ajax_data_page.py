from playwright.async_api import Page

class AjaxDataPage:
    def __init__(self, page: Page):
        self.page = page
        self.button = page.locator("#ajaxButton")
        self.result_text = page.locator(".bg-success")

    async def open(self):
        await self.page.goto("https://www.uitestingplayground.com/ajax")

    async def click_ajax_button(self):
        await self.button.click()

    async def wait_for_ajax_text(self):
        await self.page.wait_for_selector(".bg-success")
        return await self.result_text.text_content()