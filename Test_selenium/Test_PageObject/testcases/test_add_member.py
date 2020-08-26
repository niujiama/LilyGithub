from Test_selenium.Test_PageObject.page.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        self.main = MainPage()

    def teardown_class(self):
        self.main.driver.quit()

    def test_add_member(self):
        self.main.go_to_add_member().fill_in_info('小翠儿', '000004', '14523698745')
        self.main.go_to_add_member().save()

