from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

_driver = webdriver.Chrome(ChromeDriverManager().install())


def get_driver():
    _driver.implicitly_wait(20)
    return _driver
