from main.selenium_core.base_control import BaseControl


class CheckBox(BaseControl):

    def __init__(self, locator):
        self._locator = locator
        super().__init__(locator)

    def is_checked(self):
        return self.get_element().is_selected()

    def set_dynamic(self, *items):
        return CheckBox(self._dynamic_locator % items)
