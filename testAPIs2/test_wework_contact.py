import requests

class TestWework:
    corpid="wwc1b939c47f6d8e32"
    corpsecret="6e-e9pUV0QZnJppDPwzRZA9PCtKb9urb9TWNf-6v5fA"
    def get_token(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.corpid}&corpsecret={self.corpsecret}"
        r = requests.get(url)
        return r.json()["access_token"]

    def test_get(self):
        token = self.get_token()
        userid= "CeShiRenYuan"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}"
        r = requests.get(url)
        assert 0 == r.json()["errcode"]

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