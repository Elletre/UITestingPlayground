import pytest
from pages.hidden_layers_page import HiddenLayersPage


@pytest.mark.asyncio
async def test_hidden_layers(page):
    """Clicks the green button and verifies that it becomes unavailable due to the blue layer."""
    hidden_layers_page = HiddenLayersPage(page)
    await hidden_layers_page.open()
    await hidden_layers_page.click_green_button()

    assert await hidden_layers_page.is_blue_button_visible(), "Blue button should be visible after clicking the green button"
