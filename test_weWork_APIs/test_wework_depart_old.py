import requests

#从自己的企业微信中获取到企业id和通讯录的secret
corpid = "wwc1b939c47f6d8e32"
corpsecret = "6e-e9pUV0QZnJppDPwzRZA9PCtKb9urb9TWNf-6v5fA"

#获取token
def get_token():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    r = requests.get(url)
    return r.json()["access_token"]

#测试部门管理
class TestDep:
#测试创建部门
    def test_add_dep(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={get_token()}"
        json = {
                    "name": "测试部",
                    "parentid": 2,
                    "id": 8
                }
        # r = requests.post(url, json=json)
        r = requests.request('GET', url, json=json)
        assert 0 == r.json()["errcode"]

#测试部门列表
    def test_get_dep(self):
        depid= 8
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={get_token()}&id={depid}"
        r = requests.get(url)
        assert 0 == r.json()["errcode"]

#测试删除部门
    def test_del_dep(self):
        depid= 8
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={get_token()}&id={depid}"
        r = requests.get(url)
        assert 0 == r.json()["errcode"]

#测试更新部门
    def test_update_dep(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={get_token()}"
        json = {
                    "id": 7,
                    "name": "创新技术部"
                }
        r = requests.post(url, json=json)
        assert 0 == r.json()["errcode"]


