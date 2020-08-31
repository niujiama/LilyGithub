from appium.webdriver.common.mobileby import MobileBy

from Test_Appium.page.basePage import BasePage
from Test_Appium.page.contactAddPage import ContactAddPage


class MemberInvitPage(BasePage):
    def add_member_manul(self):
        _memberInvit_ele = (MobileBy.XPATH, "//*[@text='手动输入添加']")
        self.find_and_click(_memberInvit_ele)
        return ContactAddPage(self.driver)