from testAPIs2.api.baseAPI import BaseAPI
from testAPIs2.api.contactAPI import Contact

class TestWework:
    @classmethod
    def setup_class(cls):
        cls.baseApi = BaseAPI()
        cls.baseApi.get_token()

        cls.contact = Contact()

    def test_add(self):
        json = {
            "userid": "labixiaoxin",
            "name": "蜡笔小新",
            "mobile": "13426252525",
            "department": [1]
        }
        r = self.contact.add(json)
        assert 0 == r.json()["errcode"]

    def test_get(self):
        uid = "labixiaoxin"
        r = self.contact.get(uid)
        assert 0 == r.json()["errcode"]

    def test_del(self):
        uid = "labixiaoxin"
        r = self.contact.delete(uid)
        assert 0 == r.json()["errcode"]