from test_reuquest.api_page.address_page import AddressPage


class TestAddressPage:
    def setup_class(self):
        self.address_page = AddressPage()

    def test_add(self):
        self.address_page.test_add()

    def test_get(self):
        assert self.address_page.test_get()["errcode"] in [0, 60111]
