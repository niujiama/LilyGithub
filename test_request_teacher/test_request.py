import requests

corpid = "wwc1b939c47f6d8e32"
corpsecret = "6e-e9pUV0QZnJppDPwzRZA9PCtKb9urb9TWNf-6v5fA"


def get_token():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    result = requests.get(url).json()
    return result["access_token"]

def test_add():
    token = get_token()
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    data = {
        "userid": "labixiaoxin",
        "name": "蜡笔小新",
        "mobile": "10111111115",
        "department": [1]
    }
    r = requests.post(url, json=data).json()
    assert r['errcode'] in [0, 60104]

def test_get():
    token = get_token()
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=labixiaoxin"
    r = requests.get(url).json()
    assert r['errcode'] in [0, 60111]


def test_delete():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid=labixiaoxin"
    r = requests.get(url).json()
    assert r['errcode'] in [0, 60111]

def test_update():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_token()}"
    data = {
        "userid": "labixiaoxin",
        "name": "wangwu"
    }
    r = requests.post(url, json=data).json()
    assert r['errcode'] in [0, 60111]