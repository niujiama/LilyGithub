from Test_Appium.page.basePage import BasePage
from Test_Appium.page.memberInvitPage import MemberInvitPage


class ContactListPage(BasePage):
    def add_member(self):
        _contactList_ele = "添加成员"
        self.find_by_scroll_and_click(_contactList_ele)
        return MemberInvitPage(self.driver)
