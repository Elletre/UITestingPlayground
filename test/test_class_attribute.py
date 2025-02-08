import pytest
from pages.class_attribute_page import ClassAttributePage
import asyncio


@pytest.mark.asyncio
async def test_class_attribute(page):
    """Clicks a button with a specific class attribute and handles the alert"""
    class_attribute_page = ClassAttributePage(page)
    await class_attribute_page.open()
    await class_attribute_page.click_button()

    # Handle alert that appears after clicking the button
    page.on("dialog", lambda dialog: asyncio.create_task(dialog.accept()))

    assert await class_attribute_page.is_button_visible()
