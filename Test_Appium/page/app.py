from appium import webdriver
from Test_Appium.page.basePage import BasePage
from Test_Appium.page.mainPage import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            # 初始化capability
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            # 隐式等待
            self.driver.implicitly_wait(15)

        else:
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def close(self):
        self.driver.quit()

    def goto_mainPage(self) -> MainPage:
        return MainPage(self.driver)
