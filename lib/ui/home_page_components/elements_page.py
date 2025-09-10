from playwright.sync_api import Page


class ElementsPage:
    def __init__(self, page: Page):
        self.page = page

    def get_title(self) -> str:
        return self.page.title()
