import allure

@allure.feature("登录模块")
class TestFeatures:
    # @allure.story("登录成功")
    @allure.title("登录成功")
    def test_case1(self):
        pass

    @allure.story("用户名缺失")
    def test_case2(self):
        pass

    @allure.story("密码缺失")
    def test_case3(self):
        pass

    @allure.story("用户名错误")
    def test_case4(self):
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        pass

    @allure.story("密码错误")
    def test_case5(self):
        pass



