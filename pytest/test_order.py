import pytest


class TestOrder:
    @pytest.mark.run(order=3)
    def test_one(self):
        print("this is test one")

    @pytest.mark.run(order=1)
    def test_two(self):
        print("this is test two")

    @pytest.mark.run(order=2)
    def test_three(self):
        print("this is test three")

    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('a', [1, 2, 3])
    def test_four(self, a):
        print(f"this is test four, a is {a}")

    @pytest.mark.run(order=4)
    def test_five(self):
        print("this is test five")