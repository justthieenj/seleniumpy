import pytest

from main.selenium_core import browser


class TestBase:

    @pytest.fixture(autouse=True)
    def set_up(self):
        browser.maximize_browser()
        browser.open_url('https://www.google.com/')
        yield
        browser.quit_browser()
