from main.selenium_core.base_control import BaseControl


class HomePage:
    _txt_search = BaseControl("//input[@name='q']")
    _btn_search = BaseControl("//div[@style='display:none']/following-sibling::div//input[@name='btnK']")
    _lbl_first_result = BaseControl("//div[@id='rso']/div[1]//div[@class='g']/div[@data-hveid]//h3")

    def search(self, text):
        self._txt_search.enter(text)
        self._btn_search.click()

    def get_first_result(self):
        return self._lbl_first_result.get_text()
