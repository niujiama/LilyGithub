import requests
from test_request.api_page.wework_utils import WeWorkUtils
from test_request.api_page.base_api import BaseApi



class AddressPage(BaseApi):

    def __init__(self):
        self._corpsecret = "6e-e9pUV0QZnJppDPwzRZA9PCtKb9urb9TWNf-6v5fA"
        self.utils = WeWorkUtils()

    def test_get(self):
        token = self.utils._get_token(self._corpsecret)
        userid= "CeShiRenYuan"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}"
        r = requests.get(url)
        return r.json()

    def test_add(self):
        token = self.get_token()
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
        json = {
            "userid": "labixiaoxin",
            "name": "蜡笔小新",
            "mobile": "13426252525",
            "department": [1]
        }
        r = requests.post(url, json=json)
        assert 0 == r.json()["errcode"]

    def test_del(self):
        token = self.get_token()
        userid = "CeShiRenYuan"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}"
        r = requests.get(url)
        assert 0 == r.json()["errcode"]

