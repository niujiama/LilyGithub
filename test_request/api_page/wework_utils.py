import requests

from test_request.api_page.base_api import BaseApi


class WeWorkUtils(BaseApi):
    def _get_token(self, corpsecret, corpid="wwc1b939c47f6d8e32"):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url)
        return r.json()["access_token"]