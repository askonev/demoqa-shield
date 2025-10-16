from playwright.sync_api import Page, Locator


class CheckBoxTreeWidget:
    def __init__(self, page: Page, locator: Locator):
        self.page = page

        self.root_locator = locator
        self.l_expand_all = self.root_locator.locator(
            "div > button.rct-option.rct-option-expand-all"
        )
        self.l_collapse_all = self.root_locator.locator(
            "div > button.rct-option.rct-option-collapse-all"
        )
        self.l_result = self.page.locator('//*[@id="result"]')

    def expand_all(self):
        self.l_expand_all.click()
        return self

    def collapse_all(self):
        self.l_collapse_all.click()
        return self

    def toggle_root(self):
        pass

    def checkbox_root(self):
        pass

    def activate_checkbox_by_text(self, text: str):
        self.page.locator(f"//span[@class='rct-title' and text()='{text}']").click()
        return self
