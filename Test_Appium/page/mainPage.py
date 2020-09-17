from appium.webdriver.common.mobileby import MobileBy

from Test_Appium.page.basePage import BasePage
from Test_Appium.page.contactListPage import ContactListPage


class MainPage(BasePage):
    _contactList_ele = (MobileBy.XPATH, "//*[@text='通讯录']")
    def goto_contactList(self):
        self.find_and_click(self._contactList_ele)
        return ContactListPage(self.driver)

