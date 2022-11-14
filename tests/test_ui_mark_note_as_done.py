from playwright.sync_api import Page
import test_data.notes as td
from page_models.pm_main import URL_MAIN, CHECKBOX_MARK_DONE, LABEL_FIRST_NOTE

def test_ui_edit_note(page: Page, setup):
    """ Mark an existing note as done """

    page.goto(URL_MAIN)
    page.locator(CHECKBOX_MARK_DONE).click()
    page.keyboard.press('Enter')

    # Check note has been marked as done
    assert page.locator(LABEL_FIRST_NOTE).get_attribute('class') == \
        td.text_completed_note
