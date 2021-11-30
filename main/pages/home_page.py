from main.selenium_core.base_control import BaseControl


class HomePage:
    _txtSearch = BaseControl("//input[@name='q']")

    def search(self, text):
        self._txtSearch.enter(text)
