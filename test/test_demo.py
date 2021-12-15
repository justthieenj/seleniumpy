import pytest

from main.common.constants import USERNAME, PASSWORD
from main.pages.orange_hrm.login_page import LoginPage
from main.pages.orange_hrm.home_page import HomePage

from test.test_base import TestBase


class TestDemo(TestBase):
    login_page = LoginPage()
    home_page = HomePage()

    @pytest.mark.orange_hrm
    @pytest.mark.testcase
    def test_google_search(self):
        self.login_page.login(USERNAME, PASSWORD)
        self.home_page.navigate_dashboard("PIM")
        assert "a" == "a"
