from appium.webdriver.common.mobileby import MobileBy

from Test_Appium.page.basePage import BasePage


class ContactAddPage(BasePage):
    _name_ele = (MobileBy.XPATH, "//*[contains(@text, '姓名')]/../android.widget.EditText")
    _gender_ele = (MobileBy.ID, "com.tencent.wework:id/e__")
    _gender_male_ele = (MobileBy.XPATH, "//*[@text='男']")
    _gender_female_ele = (MobileBy.XPATH, "//*[@text='女']")
    _phone_ele = (MobileBy.XPATH, "//*[@text='手机号']")
    _save_ele = (MobileBy.ID, "com.tencent.wework:id/hk6")
    def add_name(self, name):
        self.find_and_sendKeys(self._name_ele, name)
        return self

    def add_gender(self, gender):
        # 性别框
        self.find_and_click(self._gender_ele)
        if gender == '男':
            # 点击男
            self.find_and_click(self._gender_male_ele)
        else:
            # 点击女
            self.find_and_click(self._gender_female_ele)
        return self
            
    def add_phone(self, phone):
        self.find_and_sendKeys(self._phone_ele, phone)
        return self

    def save(self):
        self.find_and_click(self._save_ele)
        from Test_Appium.page.memberInvitPage import MemberInvitPage
        return MemberInvitPage(self.driver)