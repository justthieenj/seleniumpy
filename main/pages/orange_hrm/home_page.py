from main.selenium_core.link import Link
from main.common.enum import SideBarMenu


class HomePage:
    __lnk_dashboard_menu = Link("//a[span[text()='%s']]")
    __lnk_submenu = Link("//a[span[text()='%s']]")

    def navigate_dashboard(self, menu_item: SideBarMenu, submenu_item):
        self.__lnk_dashboard_menu.set_dynamic(menu_item.value).click()
        self.__lnk_submenu.set_dynamic(submenu_item).click()
