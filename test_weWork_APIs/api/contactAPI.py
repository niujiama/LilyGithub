import requests
from test_weWork_APIs.api.baseAPI import BaseAPI

class Contact:
    def add(self, json):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create", json=json,
                         params={"access_token": BaseAPI.token})
        return r

    def get(self, uid):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/get",
                         params={
                             "access_token": BaseAPI.token,
                             "userid": uid
                         })
        return r

    def delete(self, uid):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/delete",
                         params={
                             "access_token": BaseAPI.token,
                             "userid": uid
                         })
        return r
