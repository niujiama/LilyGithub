from appium import webdriver
from appium.webdriver import webdriver, WebElement
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _driver: WebDriver = None
    _current_element: WebElement = None
    def start(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = "true"
        self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self._driver.implicitly_wait(20)
        return self

    def stop(self):
        self._driver.quit()

    def find(self, by):
        self._current_element = self._driver.find_element(*by)
        return self

    def click(self):
        self._current_element.click()
        return self

    def send_keys(self):
        pass