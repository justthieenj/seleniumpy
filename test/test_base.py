import unittest
import pytest

from main.selenium_core import browser


class TestBase(unittest.TestCase):

    @pytest.fixture(scope="session", autouse=True)
    def setUp(self):
        browser.maximize_browser()
        browser.open_url('https://www.google.com/')
        yield
        browser.quit_browser()
