from main.selenium_core import driver_manager

_driver = driver_manager.get_driver()


def open_url(url):
    _driver.get(url)


def maximize_browser():
    _driver.maximize_window()


def quit_browser():
    _driver.quit()


def close_browser():
    _driver.close()
