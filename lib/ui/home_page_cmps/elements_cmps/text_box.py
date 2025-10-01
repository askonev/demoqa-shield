import os
from typing import Dict
from playwright.sync_api import Page

from lib.framework.file_handler import FileHandler


class TextBox:
    def __init__(self, page: Page):
        self.page = page
        self.submit = self.page.locator("//*[@id='submit']")
        self.result_p = self.page.locator("//*[@id='output']/div/p[@id='name']")

    def set_text(self, data: Dict[str, str]) -> object:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(script_dir, "text_box_locators.json")
        locators = FileHandler().import_json(json_path)

        for field, field_data in data.items():
            self.page.fill(locators[field], field_data)

    def submit_click(self):
        self.submit.click()

    def result_text(self):
        return self.result_p.text_content()
