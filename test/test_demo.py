from main.pages.home_page import HomePage

from test.test_base import TestBase


class TestDemo(TestBase):
    home_page = HomePage()

    def test_google_search(self):
        self.home_page.search('youtube')
        assert 'str' == 'str1', 'Error message'
