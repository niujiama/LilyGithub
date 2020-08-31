from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        # 初始化driver
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        self.find(locator).click()

    def find_and_sendKeys(self, locator, value):
        self.find(locator).send_keys(value)

    def find_by_scroll_and_click(self, text):
        element = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector()'
                   '.scrollable(true).instance(0))'
                   '.scrollIntoView(new UiSelector()'
                   f'.text("{text}").instance(0));')
        self.find(element).click()

    def get_toast(self):
        _toast_ele = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")
        text = self.find(_toast_ele).text
        return text


