import pytest

from Test_Appium.page.app import App


class TestCase:
    def setup(self):
        '''
        启动app
        '''
        self.app = App()
        self.main = self.app.start().goto_mainPage()

    def teardown(self):
        self.app.close()

    # @pytest.mark.dependency()
    # @pytest.mark.parametrize('name, gender, phoneNum', [("人员", "女", "13526287412")])
    def test_addContact(self):
        name = "测试人员"
        gender = '女'
        phone = '1234567899'
        page = self.main.goto_contactList().add_member().add_member_manul()\
            .add_name(name).add_gender(gender).add_phone(phone).save()
        toast = page.get_toast()
        assert toast == '添加成功'

    # @pytest.mark.parametrize('name,gender,phonenum', get_contact())
    # def test_addcontact(self, name, gender, phonenum):
    #     mypage = self.main.goto_addresslist().add_member().addmember_menual() \
    #         .edit_name(name).edit_gender(gender).edit_phonenum(phonenum) \
    #         .click_save()
    #
    #     mytoast = mypage.get_toast()
    #     assert mytoast == '添加成功'



    # @pytest.mark.dependency(depends=["TestCase::test_addContact"])
    # # @pytest.mark.parametrize('name', [("人员")])
    # def test_delContact(self):
    #     name = '测试人员'
    #     print(f'{name} will be deleted')
    #     assert 2 == 2