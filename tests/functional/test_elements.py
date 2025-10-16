import pytest
from faker import Faker
from playwright.sync_api import Page, expect

from lib.ui.home_page import HomePage
from lib.ui.home_page_cmps.elements_page import ElementsPage


@pytest.fixture
def home(page: Page) -> HomePage:
    return HomePage(page)


@pytest.fixture
def elements(home: HomePage) -> ElementsPage:
    home.goto()
    return home.goto_elements_page()


@pytest.mark.e2e
def test_elements_page_title_is_correct(elements: ElementsPage):
    assert elements.get_title() == "DEMOQA"


@pytest.mark.e2e
def test_text_box_submission(elements: ElementsPage):
    elements.dropdown_elements_click()
    text_box = elements.goto_text_box()

    fake = Faker()

    data = {
        "Full Name": fake.name(),
        "Email": fake.email(),
        "Current Address": fake.address(),
        "Permanent Address": fake.address(),
    }

    text_box.set_text(data)
    text_box.submit.click()
    result = text_box.result_text()
    assert "Name:" + data["Full Name"] == result


@pytest.mark.e2e
def test_check_box_selected_all(elements: ElementsPage):
    check_box = elements.dropdown_elements_click().goto_check_box()
    expect(
        check_box.tree.expand_all().activate_checkbox_by_text("Commands").l_result
    ).to_have_text("You have selected :commands")
