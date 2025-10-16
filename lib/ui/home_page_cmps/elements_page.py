from playwright.sync_api import Page

from .elements_cmps.text_box import TextBox
from .elements_cmps.check_box import CheckBox


class ElementsPage:
    def __init__(self, page: Page):
        self.page = page
        self.text_box = self.page.locator("//span[text()='Text Box']/parent::li")
        self.check_box = self.page.locator("//span[text()='Check Box']/parent::li")
        self.dropdown_elements = self.page.locator(
            "//div[@class='header-text' and text()='Elements']/ancestor::span"
        )

    def get_title(self) -> str:
        return self.page.title()

    def dropdown_elements_click(self):
        self.dropdown_elements.click()
        return self

    def goto_text_box(self) -> TextBox:
        self.text_box.click()
        return TextBox(self.page)

    def goto_check_box(self) -> CheckBox:
        self.check_box.click()
        return CheckBox(self.page)
