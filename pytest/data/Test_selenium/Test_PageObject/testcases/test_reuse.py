from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

"""
前提：
1. 关闭chrome
2. 在cmd运行：chrome -remote-debugging-port=9222
3. 打开要复用的网址，登录
4. 运行下面的用例
"""


class TestReUse():
    def setup(self):
        option = Options()
        option.debugger_address = 'localhost:9222'
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def test_open(self):
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        self.driver.find_element(By.CSS_SELECTOR, '.ww_indexImg_AddMember').click()
