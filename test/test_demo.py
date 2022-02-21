import pytest

from main.common.enum import SideBarMenu
from main.common.constants import USERNAME, PASSWORD
from main.pages.orange_hrm.login_page import LoginPage
from main.pages.orange_hrm.home_page import HomePage
from main.pages.orange_hrm.pim_page import PIMPage

from test.test_base import TestBase


class TestDemo(TestBase):
    login_page = LoginPage()
    home_page = HomePage()
    pim_page = PIMPage()

    @pytest.mark.orange_hrm
    @pytest.mark.testcase
    def test_get_table_data(self):
        self.login_page.login(USERNAME, PASSWORD)
        self.home_page.navigate_dashboard(SideBarMenu.PIM, "Employee List")
        cell_value = self.pim_page.get_value("1058", "Name")

        print("\nActual value: " + cell_value)

        assert "Peter Anderson" == cell_value

        print("\nTest Passed")
