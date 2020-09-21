import pytest


class TestFixture:
    @pytest.fixture()
    def login(self):
        print("this is login")
        return ("tom", "123")

    @pytest.fixture()
    def operate(self):
        print("this is operate")

    def test_case1(self, login, operate):
        print("login + operate")

    def test_case2(self, login):
        print("only login")

    def test_case(self):
        print("no login and operate")
