import pytest
from playwright.sync_api import Page
from lib.ui.elements_page import ElementPage


@pytest.mark.parametrize("url", ["https://demoqa.com/elements"])
def test_page_headers_is_correct(page: Page, url: str):
    elements_page = ElementPage(page)
    elements_page.goto(url)
    assert elements_page.get_title() == "DEMOQA"
