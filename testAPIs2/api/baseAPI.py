import requests

class BaseAPI:
    token = ""

    @classmethod
    def get_token(cls):
        cls.token = ""
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params={
                             "corpid": "wwc1b939c47f6d8e32",
                             "corpsecret": "6e-e9pUV0QZnJppDPwzRZA9PCtKb9urb9TWNf-6v5fA"
                         })
        cls.token = r.json()["access_token"]