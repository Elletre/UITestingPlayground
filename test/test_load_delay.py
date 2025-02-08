import pytest
from pages.load_delay_page import LoadDelayPage


@pytest.mark.asyncio
async def test_load_delay(page):
    """Waits for the delayed button to appear and verifies its visibility."""
    load_delay_page = LoadDelayPage(page)
    await load_delay_page.open()

    assert await load_delay_page.wait_for_button(), "Button did not appear after delay"