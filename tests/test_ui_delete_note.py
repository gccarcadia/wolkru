from playwright.sync_api import Page
import test_data.notes as td
from page_models.pm_main import URL_MAIN, BUTTON_DELETE_NOTE, LABEL_FIRST_NOTE

def test_ui_delete_note(page: Page, setup):
    """ Delete an existing note """

    page.goto(URL_MAIN)
    page.locator(LABEL_FIRST_NOTE).hover()
    page.locator(BUTTON_DELETE_NOTE).click()

    # Check if note has been deleted
    assert page.locator(LABEL_FIRST_NOTE).count() == 0
