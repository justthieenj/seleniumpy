from main.selenium_core import driver_manager


class BaseControl:
    _locator = None
    _driver = driver_manager.get_driver()

    def __init__(self, locator):
        self._locator = locator

    def get_element(self):
        return self._driver.find_element_by_xpath(self._locator)

    def click(self):
        self.get_element().click()

    def enter(self, text):
        self.get_element().send_keys(text)
