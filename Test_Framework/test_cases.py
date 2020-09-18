import pytest

from Test_Framework.demo_page import DemoPage


class TestCases:
    def setup_class(self):
        self.demo = DemoPage()
        self.demo.start()

    def teardown_class(self):
        self.demo.stop()

    @pytest.mark.parametrize('username, password', [
        ('user1', 'password1'),
        ('user2', 'password2')
    ])
    def test_login(self, username, password):
        #todo: 用例的数据驱动
        self.demo.login(username, password)
        assert 1 == 1

    @pytest.mark.parametrize('keyword', [
        'alibaba'
        # 'baidu',
        # 'jd'
    ])
    def test_search(self, keyword):
        self.demo.search(keyword)