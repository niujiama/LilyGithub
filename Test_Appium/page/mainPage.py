from appium.webdriver.common.mobileby import MobileBy

from Test_Appium.page.basePage import BasePage
from Test_Appium.page.contactListPage import ContactListPage


class MainPage(BasePage):

    def goto_contactList(self):
        _contactList_ele = (MobileBy.XPATH, "//*[@text='通讯录']")
        self.find_and_click(_contactList_ele)
        return ContactListPage(self.driver)

