from test_request_teacher.api_page.base_api import BaseApi


class WeWorkUtils(BaseApi):
    def get_token(self, corpsecret, corpid="wwc1b939c47f6d8e32"):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {"corpid": corpid, "corpsecret": corpsecret}
        }

        result = self.send_api(data)
        return result["access_token"]

a = WeWorkUtils()
print(a.get_token('6e-e9pUV0QZnJppDPwzRZA9PCtKb9urb9TWNf-6v5fA'))
