import time

import requests
from test_reuquest.api_page.wework_utils import WeWorkUtils
from test_reuquest.api_page.base_api import BaseApi


class AddressPage(BaseApi):

    def __init__(self):
        self._corpsecret = "6e-e9pUV0QZnJppDPwzRZA9PCtKb9urb9TWNf-6v5fA"
        self.utils = WeWorkUtils()
        self.token = self.utils._get_token(self._corpsecret)
        self.userid = 'testUser' + str(int(time.time()))
        print(self.userid)

    def test_get(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={self.userid}"
        r = requests.get(url)
        return r.json()

    def test_add(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        json = {
            "userid": f"{self.userid}",
            "name": "蜡笔小新",
            "mobile": "13426252525",
            "department": [1]
        }
        r = requests.post(url, json=json)
        return r.json()

    def test_del(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={self.userid}"
        r = requests.get(url)
        return r.json()
