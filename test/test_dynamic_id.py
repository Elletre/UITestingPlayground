import pytest
from pages.dynamic_id_page import DynamicIDPage

@pytest.mark.asyncio
async def test_dynamic_id(page):
    """Clicks a button with a dynamic ID using Page Object pattern"""
    dynamic_id_page = DynamicIDPage(page)
    await dynamic_id_page.open()
    await dynamic_id_page.click_button()
    assert await dynamic_id_page.is_button_visible()
