from playwright.sync_api import Page

from lib.ui.home_page_cmps.elements_cmps.text_box import TextBox


class ElementsPage:
    def __init__(self, page: Page):
        self.page = page
        self.text_box = self.page.locator("//span[text()='Text Box']/parent::li")
        self.dropdown_elements = self.page.locator(
            "//div[@class='header-text' and text()='Elements']/ancestor::span"
        )

    def get_title(self) -> str:
        return self.page.title()

    def dropdown_elements(self):
        self.dropdown_elements.click()

    def goto_text_box(self) -> TextBox:
        self.text_box.click()
        return TextBox(self.page)
