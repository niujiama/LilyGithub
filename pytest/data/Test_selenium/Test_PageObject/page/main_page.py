from pytest.data.Test_selenium.Test_PageObject.page.base_page import BasePage
from pytest.data.Test_selenium.Test_PageObject.page.contact_page import ContactPage
from pytest.data.Test_selenium.Test_PageObject.page.add_member_page import AddMemberPage

class MainPage(BasePage):
    _url = 'https://work.weixin.qq.com/wework_admin/frame#index'
    def go_to_contact(self):
        return ContactPage(self.driver)

    def go_to_add_member(self):
        self.driver.find_element(By.CSS_SELECTOR, '.ww_indexImg_AddMember').click()
        return AddMemberPage(self.driver)