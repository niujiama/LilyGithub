import pytest


class TestCase:

    @pytest.mark.dependency()
    # @pytest.mark.parametrize('name, gender, phoneNum', [("人员", "女", "13526287412")])
    def test_addContact(self):
        name = "人员"
        gender = '女'
        phoneNum = '1234567899'
        print(f'{name} is {gender}, his phoneNum is {phoneNum}')
        assert 1 == 1


    @pytest.mark.dependency(depends=["TestCase::test_addContact"])
    # @pytest.mark.parametrize('name', [("人员")])
    def test_delContact(self):
        name = '人员'
        print(f'{name} will be deleted')
        assert 2 == 2