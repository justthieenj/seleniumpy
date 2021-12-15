from main.selenium_core.base_control import BaseControl


class HomePage:
    __txt_username = BaseControl("#txtUsername")
    __txt_password = BaseControl("#txtPassword")
    __btn_login = BaseControl("#btnLogin")

    def login(self, username, password):
        self.__txt_username.enter(username)
        self.__txt_password.enter(password)
        self.__btn_login.click()
