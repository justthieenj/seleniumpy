from main.pages.home_page import HomePage

from main.selenium_core import browser
from test.test_base import TestBase


class TestDemo(TestBase):
    home_page = HomePage()

    def test_google_search(self):
        browser.open_url('https://www.google.com/')
        self.home_page.search('youtube')
        assert 'str' in 'str'
