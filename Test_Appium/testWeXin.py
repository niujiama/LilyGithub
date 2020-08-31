
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
# pip install appium-python-client 里面提供的api
from time import sleep, time

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDemo:
    def setup_class(self):
        #初始化capability
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待
        self.driver.implicitly_wait(15)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.dependency()
    def test_addOne(self, name='测试添加', gender='男', phoneNum='13288889999'):
        '''
        用例标题：添加联系人
        前提条件
            已登录状态（ noReset=True）
        用例步骤：
            1、打开【企业微信】应用
            2、进入【通讯录】
            3、点击【添加成员】
            4、在添加成员页面点击【手动输入添加】
            5、输入【姓名】【性别】【手机号】
            6、点击【保存】
            7、验证保存成功
            8、返回【通讯录】
        '''
        # name = name
        # gender = gender
        # phoneNum = phoneNum
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../android.widget.EditText").send_keys(name)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/e__").click()
        if gender == '男':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phoneNum)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hk6").click()
        toasttext = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert '添加成功' == toasttext
        self.driver.back()
        print('添加成功')

    @pytest.mark.dependency(depends=['TestDemo::test_addOne'])
    def test_delOne(self, name='测试添加'):
        '''
        用例标题：删除联系人
        前提条件
            已登录状态（ noReset=True）
        用例步骤：
            1、新建【删除用户】（调用新建联系人方法）
            2、点击【删除用户】，进入【个人信息】
            3、点击【。。。】，进入更多页面
            4、点击【编辑成员】，进入编辑成员
            5、点击【删除成员】
            6、在确认弹框中，点击【删除】
            7、等待3秒，断言【通讯录】中不存在【删除用户】？？？要研究下怎么做到
        '''
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 查找当前页面name的元素们
        preEles = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        # 点击找到的第一个name元素
        self.driver.find_element(MobileBy.XPATH,  f"//*[@text='{name}']").click()
        #点击。。。
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/hjz']").click()
        # 点击【编辑成员】
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b53']").click()
        # 点击【删除成员】
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("删除成员").instance(0));').click()
        # 点击【删除】
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/bfe']").click()
        sleep(2)
        curEles = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        preNum = len(preEles)
        curNum = len(curEles)
        assert preNum == (curNum + 1)
        print('删除成功！')

    # def test_addcontact(self):
    #     '''
    #     企业微信：添加联系人测试用例
    #     前提条件
    #         已登录状态（ noReset=True）
    #     打卡用例：
    #         1、打开【企业微信】应用
    #         2、进入【通讯录】
    #         3、点击【添加成员】
    #         4、在添加成员页面点击【手动输入添加】
    #         5、输入【姓名】【性别】【手机号】
    #         6、点击【保存】
    #         7、验证保存成功
    #     '''
    #     name = "测试用户"
    #     gender = '男'
    #     phoneNum = "13900000002"
    #
    #     self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
    #     self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
    #     self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
    #     self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(name)
    #     self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
    #     if gender == '男':
    #         self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
    #     else:
    #         self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
    #
    #     self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/emh").send_keys(phoneNum)
    #     self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq7").click()
    #     # sleep(2)
    #     # toast 弹框,打印当前页面的布局结构 ，xml 结构
    #     # print(self.driver.page_source)
    #     toasttext = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
    #     assert '添加成功' == toasttext