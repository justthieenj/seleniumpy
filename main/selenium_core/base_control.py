from main.selenium_core import driver_manager
from selenium.webdriver.common.by import By


class BaseControl:
    _locator = None
    _by = None
    _driver = driver_manager.get_driver()

    def __init__(self, locator):
        self._locator = locator
        self._by = By.XPATH if locator.startswith("//") else By.CSS_SELECTOR

    def get_element(self):
        return self._driver.find_element(self._by, self._locator)

    def get_elements(self):
        return self._driver.find_elements(self._by, self._locator)

    def click(self):
        self.get_element().click()

    def enter(self, text):
        self.get_element().send_keys(text)

    def get_text(self):
        return self.get_element().text
