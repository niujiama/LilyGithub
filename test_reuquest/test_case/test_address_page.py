import pytest
import pytest_ordering

from test_reuquest.api_page.address_page import AddressPage


class TestAddressPage:
    def setup_class(self):
        self.address_page = AddressPage()

    @pytest.mark.run(order=1)
    def test_add(self):
        r = self.address_page.test_add()
        assert r['errcode'] == 0

    @pytest.mark.run(order=2)
    def test_get(self):
        r = self.address_page.test_get()
        assert r['errcode'] == 0

    @pytest.mark.run(order=3)
    def test_del(self):
        r = self.address_page.test_del()
        assert r['errcode'] == 0
