from main.selenium_core.base_control import BaseControl


class HomePage:
    _txtSearch = BaseControl("//input[@name='q']")

    def __init__(self):
        pass

    def search(self, text):
        self._txtSearch.enter(text)
