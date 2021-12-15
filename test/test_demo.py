import pytest

from main.common.constants import USERNAME, PASSWORD
from main.pages.orange_hrm.home_page import HomePage

from test.test_base import TestBase


class TestDemo(TestBase):
    home_page = HomePage()

    @pytest.mark.orange_hrm
    @pytest.mark.testcase
    def test_google_search(self):
        self.home_page.login(USERNAME, PASSWORD)
        assert "a" == "a"
