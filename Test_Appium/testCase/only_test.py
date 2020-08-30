import pytest


class TestCase:
    @pytest.mark.dependency()
    def test_01(self):
        assert 2==1

    @pytest.mark.dependency(depends=['TestCase::test_01'])
    def test_02(self):
        assert 3==3

