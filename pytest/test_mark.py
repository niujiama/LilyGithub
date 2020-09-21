import pytest


class TestMark:
    @pytest.mark.smoke
    def test_mark1(self):
        print("this is test_mark1")

    @pytest.mark.middle
    def test_mark2(self):
        print("this is test_mark2")

    @pytest.mark.low
    def test_mark3(self):
        print("this is test_mark3")