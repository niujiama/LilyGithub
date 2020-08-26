from Test_selenium.Test_PageObject.page.base_page import BasePage


class AddMemberPage(BasePage):
    def fill_in_info(self, username, accid, phone):
        self.driver.find_element(By.ID, 'username').send_keys(username)
        self.driver.find_element(By.ID, 'memberAdd_aacid').send_keys(accid)
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys(phone)

    def save(self):
        self.driver.find_element(By.CSS_SELECTOR, '.qui_btn ww_btn js_btn_save').click()

    def save_and_add(self):
        pass

    def cancel(self):
        pass


