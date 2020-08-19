from selenium import webdriver
import time

class TestHogwarts():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_hogwarts(self):
        self.driver.get('https://ceshiren.com/')
        time.sleep(3)
        self.driver.find_element_by_id('ember187').click()
        time.sleep(3)
        self.driver.find_element_by_link_text('雪球app抓不到包').click()
        time.sleep(3)


