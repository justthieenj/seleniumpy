from main.selenium_core.base_control import BaseControl


class Link(BaseControl):

    def __init__(self, locator):
        self._locator = locator
        super().__init__(locator)

    def get_href(self):
        return self.get_element().get_attribute("href")

    def set_dynamic(self, *items):
        return Link(self._dynamic_locator % items)
