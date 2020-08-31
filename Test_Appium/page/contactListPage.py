from Test_Appium.page.basePage import BasePage
from Test_Appium.page.memberInvitPage import MemberInvitPage


class ContactListPage(BasePage):
    _contactList_ele = "添加成员"
    def add_member(self):
        self.find_by_scroll_and_click(self._contactList_ele)
        return MemberInvitPage(self.driver)
