import pytest

class TestMutiParas:

    @pytest.mark.parametrize("a", [1, 2])
    @pytest.mark.parametrize("b", [3, 4, 5])

    def test_foo(self, a, b):
        print(f"this is {a}, {b}")