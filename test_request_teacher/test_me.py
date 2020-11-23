import requests

corpid = "wwc1b939c47f6d8e32"
corpsecret = "6e-e9pUV0QZnJppDPwzRZA9PCtKb9urb9TWNf-6v5fA"


def get_token():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    result = requests.get(url).json()
    return result["access_token"]

def test_get():
    token = get_token()
    print(token)
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=zhangsan"
    r = requests.get(url).json()
    print(r)
    assert r['errcode'] in [0, 60111]

def test_baidu():
    r = requests.get('http://baidu.com')
    print(r.json())