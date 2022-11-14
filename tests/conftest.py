import pytest
from playwright.sync_api import Page
import test_data.notes as td
from page_models.pm_main import URL_MAIN, INPUT_CREATE_NOTE


@pytest.fixture(scope="function")
def setup(page: Page):
    """ Creates a note to setup some tests """
    
    page.goto(URL_MAIN)
    page.locator(INPUT_CREATE_NOTE).fill(td.text_first_note)
    page.keyboard.press('Enter')
