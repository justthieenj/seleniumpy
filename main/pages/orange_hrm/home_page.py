from main.selenium_core.link import Link


class HomePage:
    __lnk_dashboard_menu = Link("//a[b[text()='%s']]")

    def navigate_dashboard(self, name):
        self.__lnk_dashboard_menu.set_dynamic(name).click()
