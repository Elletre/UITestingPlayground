import pytest
from pages.ajax_data_page import AjaxDataPage


@pytest.mark.asyncio
async def test_ajax_data(page):
    """Clicks the AJAX button and verifies that data loads after a delay"""
    ajax_data_page = AjaxDataPage(page)
    await ajax_data_page.open()
    await ajax_data_page.click_ajax_button()

    result_text = await ajax_data_page.wait_for_ajax_text()

    assert "Data loaded with AJAX" in result_text, "Expected AJAX-loaded text not found"