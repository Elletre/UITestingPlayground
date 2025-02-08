import pytest
from pages.text_input_page import TextInputPage


@pytest.mark.asyncio
async def test_text_input(page):
    """Enters text in the input field, clicks the button, and verifies the button text updates."""
    test_button_text = "Test Text"
    text_input_page = TextInputPage(page)
    await text_input_page.open()

    await text_input_page.enter_text(test_button_text)
    await text_input_page.click_button()

    button_text = await text_input_page.get_button_text()
    assert button_text.strip() == test_button_text, f"Expected '{test_button_text}', but got '{button_text.strip()}'"
