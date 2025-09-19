from playwright.sync_api import Page

from lib.ui.home_page_cmps.elements_page import ElementsPage


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://demoqa.com/"
        self.elements_link = self.page.locator(
            "//h5[text()='Elements']/ancestor::div[@class='category-cards']"
        )

    def goto(self):
        self.page.goto(self.url)

    def goto_elements_page(self) -> ElementsPage:
        self.elements_link.click()
        return ElementsPage(self.page)
