from main.selenium_core.base_control import BaseControl
from main.selenium_core.textbox import TextBox


class LoginPage:
    __txt_username = TextBox("#txtUsername")
    __txt_password = TextBox("#txtPassword")
    __btn_login = BaseControl("#btnLogin")

    def login(self, username, password):
        self.__txt_username.enter(username)
        self.__txt_password.enter(password)
        self.__btn_login.click()
