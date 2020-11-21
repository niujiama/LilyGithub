import pytest


class TestFixture:
    @pytest.fixture()   #装饰器
    def login(self):
        print("this is login")
        return ("tom", "123")

    @pytest.fixture()
    def operate(self):
        print("this is operate")
        # return "opertate"

    def test_case1(self, login, operate):   #装饰器可以作为参数传入
        # 装饰器还能作为变量输出，输出值就是装饰器的返回值
        print(f"login {login} + operate {operate}")


    def test_case2(self, login):
        print(f"only login {login}")

    def test_case(self):
        print("no login and operate")
