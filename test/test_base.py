import pytest

from main.common.constants import URL
from main.selenium_core import browser


class TestBase:

    @pytest.fixture(autouse=True)
    def test_base(self):
        print("setup")
        browser.maximize_browser()
        browser.open_url(URL)
        yield
        print("\nteardown")
        browser.quit_browser()
