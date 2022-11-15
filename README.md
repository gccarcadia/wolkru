# Install dependencies
- Install Python (3.7 + required) and add pip and python executable to path
- Run `pip install -r requirements.txt` from the root project folder
- Run `playwright install`

# How to run tests
- Run tests using headless browser (default) : `python -m pytest -v tests`
- Run tests with headed browser: `python -m pytest -v --headed tests`
- Run tests with specific browser: `python -m pytest -v --browser firefox --headed`
 (can be `chromium`, `firefox`, or `webkit`)

- For additional information, please refer to those pages:
  - `https://playwright.dev/python/docs/intro`
  - `https://playwright.dev/python/docs/test-runners`.

# Bugs in application from https://github.com/OlenaPletnova/Manual-test-exercise/releases/tag/excercise:
- Edit - application crashes on trying to edit when no entry is selected:

  From Windows event viewer:

  Faulting application name: Addresser.exe, version: 1.0.0.0, time stamp: 0x58da34d6
  Faulting module name: KERNELBASE.dll, version: 10.0.19041.2193, time stamp: 0x7f7062e1
  Exception code: 0xe0434352
  Fault offset: 0x000000000002cd29
  Faulting process id: 0x5fec
  Faulting application start time: 0x01d8f6051ceefa5e
  Faulting application path: D:\Klaw\Personale\Jobs\Wolters-Kruger\Addresser.exe
  Faulting module path: C:\Windows\System32\KERNELBASE.dll
  Report Id: 2fa54e4a-8696-4177-8a21-14560545e07d
  Faulting package full name: 
  Faulting package-relative application ID: 

- File - Export > there is no confirmation or prompt where to save the exported contacts (the contacts are saved in the working directory in the file "Exported_contacts.txt", but the file is overwritten each time)

- The entries in the address book should be sortable by columns

- It would be nice to have an import feature, just like there is the export feature

- You can completely hide all of the columns by resizing them and there is no indication that there was a column

- Exporting the contents does not maintain the order of the columns if the column order was previously changed

- The order of the fields is different when adding an entry and when editing an entry
  - Add: Name, Phone number, Address, Email, Comments
  - Edit: Name, Address, Phone number, Email, Comments

- Edit - An entry can be saved without the phone number, even if the phone number is marked as mandatory

- Edit - Internal error when trying to add a duplicate entry with the same name and same phone number

- Phone number length is limited to only 12 digits, but there are international phone numbers with more than 12 digits

- Can add spaces after the phone number and the spaces are also exported
