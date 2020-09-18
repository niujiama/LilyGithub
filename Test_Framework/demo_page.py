from selenium.webdriver.common.by import By

from Test_Framework.base_page import BasePage


class DemoPage(BasePage):
    #todo: po的数据驱动
    _search_button = (By.ID, 'home_search')
    def login(self, username, password):
        pass

    def forget_password(self):
        pass

    def search(self, keyword):
        self.find(self._search_button).click()
        return self