from main.selenium_core.base_control import BaseControl


class PIMPage:
    __dynamic_element = BaseControl(
        "//table[@id='employeeListTable']//tr[count(//table[@id='employeeListTable']/tbody/tr[td[text()='%s']]/preceding-sibling::tr)+1]/td[count(//table[@id='employeeListTable']//th[text()='%s']/preceding-sibling::th)+1]")

    def get_value(self, employee_id, header):
        return self.__dynamic_element.set_dynamic(employee_id, header).get_text()
