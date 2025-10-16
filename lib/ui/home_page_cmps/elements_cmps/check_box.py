from playwright.sync_api import Page

from .check_box_tree_widget import CheckBoxTreeWidget


class CheckBox:
    def __init__(self, page: Page):
        self.page = page
        self.tree_container = self.page.locator('//*[@id="tree-node"]')
        self.tree = CheckBoxTreeWidget(self.page, self.tree_container)
