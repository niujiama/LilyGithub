import pytest


class TestOrder:
    @pytest.mark.parametrize()
    @pytest.mark.run(order=3)
    def test_one(self):
        print("this is test one")

    @pytest.mark.run(order=1)
    def test_two(self):
        print("this is test two")

    @pytest.mark.run(order=2)
    def test_three(self):
        print("this is test three")

    def test_four(self):
        print("this is test four")

    def test_five(self):
        print("this is test five")