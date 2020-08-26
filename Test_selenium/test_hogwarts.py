from selenium import webdriver
import time

class TestHogwarts():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_hogwarts(self):
        self.driver.get('https://ceshiren.com/')
        self.driver.find_element_by_link_text('热门').click()
        self.driver.find_element_by_link_text('测试人社区在线沙龙第三期答疑帖').click()



