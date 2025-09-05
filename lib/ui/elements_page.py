from lib.ui.base_page import BasePage
from playwright.sync_api import Page


class ElementPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # self.header = page.locator(".main-header")
