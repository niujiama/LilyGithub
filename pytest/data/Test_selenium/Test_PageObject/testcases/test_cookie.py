from typing import List, Dict
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pytest
import json

'''
1. 运行test_weixin_sleep方法
2. 手机马上扫码，运行完test_weixin_sleep方法获取cookies
3. 再运行test_weixin，就可以跑用例了
'''

class TestChains():
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_weixin_sleep(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        sleep(30)
        cookies = self.driver.get_cookies()
        with open("data/cookies.txt", "w") as f:
            json.dump(cookies, f)

    @pytest.mark.skip
    def test_weixin(self):
        # 先打开企业微信的页面，才能传cookies进去
        self.driver.get("https://work.weixin.qq.com/")

        with open("data/cookies.txt", "r") as f:
            # 从文件获取cookies，并转化成list对象
            cookies: List[Dict] = json.load(f)
        # 遍历每一条cookies，把登录的cookies传入到企业微信中
        for cookie in cookies:
            # 由于selenium的cookies不支持expiry，所以需要去掉
            if "expiry" in cookie.keys():
                # dict支持pop的删除函数
                cookie.pop("expiry")
            # 添加cookies
            self.driver.add_cookie(cookie)
        # 再打开企业微信登录后的页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(5)