from playwright.sync_api import Page
import test_data.notes as td
from page_models.pm_main import URL_MAIN, INPUT_EDIT_NOTE, LABEL_FIRST_NOTE

def test_ui_edit_note(page: Page, setup):
    """ Edit an existing note """

    page.goto(URL_MAIN)
    page.locator(LABEL_FIRST_NOTE).dblclick()
    page.locator(INPUT_EDIT_NOTE).fill(td.text_edited_note)
    page.keyboard.press('Enter')

    # Check if the note has been edited
    assert page.locator(LABEL_FIRST_NOTE).inner_text() == td.text_edited_note
