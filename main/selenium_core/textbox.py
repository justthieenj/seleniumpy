from main.selenium_core.base_control import BaseControl


class TextBox(BaseControl):

    def __init__(self, locator):
        self._locator = locator
        super().__init__(locator)

    def enter(self, text):
        self.get_element().send_keys(text)
