from playwright.sync_api import Page


class TextBox:
    def __init__(self, page: Page):
        self.page = page
