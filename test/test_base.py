import pytest

from main.selenium_core import browser


class TestBase:
    @pytest.fixture(autouse=True)
    def test_base(self):
        print("setup")
        browser.maximize_browser()
        browser.open_url("https://www.google.com/")
        yield
        print("teardown")
        browser.quit_browser()
