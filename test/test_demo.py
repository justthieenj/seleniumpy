from main.pages.home_page import HomePage

from test.test_base import TestBase


class TestDemo(TestBase):
    home_page = HomePage()

    def test_google_search(self):
        _search_value = 'youtube'
        self.home_page.search(_search_value)
        _result = self.home_page.get_first_result()
        assert _search_value in _result.lower(), f"First result should contains text '{_search_value}'"
