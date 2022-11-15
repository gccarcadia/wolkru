from playwright.sync_api import Page
import test_data.notes as td
from page_models.pm_main import URL_MAIN, INPUT_CREATE_NOTE, LABEL_FIRST_NOTE

def test_ui_add_note(page: Page):
    """ Add a note """

    page.goto(URL_MAIN)
    page.locator(INPUT_CREATE_NOTE).fill(td.text_first_note)
    page.keyboard.press('Enter')

    # Check if the note has been added
    assert page.locator(LABEL_FIRST_NOTE).inner_text() == td.text_first_note
