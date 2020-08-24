"""
1、要先获取到企业微信的cookie
    -采用复用已有浏览器的方式（只能使用chrome，window先把chrome快捷方式地址配置到path环境变量，关闭所有chrome浏览器页面，命令行执行chrome --remote-debugging-port=9222）
    -再打开的chrome浏览器中登录企业微信后台管理账号
    -在setup方法中，设置调试器地址 (debugger_address)，设置的端口号与命令行执行的一致，引用option时要注意引用chrome的，代码语句如下：
        option = Options()
        option.debugger_address = "localhost:9222"
    -在实例化driver对象时，注意此处是chrome的，然后参数方法要使用options=，代码语句如下：
        self.driver = webdriver.Chrome(options=option)
2、在test_cookie方法中，要先去获取cookie，使用driver.get_cookies方法，并在控制台输出以便使用，代码语句如下：
    cookies = self.driver.get_cookies()
    print(cookies)
3、然后执行test_cookie方法，获取到cookies，在控制台复制并赋值给自定义变量cookies
4、此时已获取到cookies，则实例化driver时，不再需要复用浏览器cookie，即把实例化中参数删去；并且不需要重复获取和输出cookies，即注释掉2、中的代码
5、使用for循环和driver.add_cookie方法将cookie添加，用以完成登录验证(添加cookie如果遇到浮点型的参数，运行会报错，这种情况，可以去做处理，在for循环中添加if判断，通过对应key值判断，pop删除这个值)
6、然后就可以进行登陆后的操作验证等
"""
import shelve

from Test_selenium.Base import Base

class TestExport(Base):
    def test_cookie(self):
        # cookies = self.driver.get_cookies()
        # print(cookies)
        cookies = [{'domain': 'work.weixin.qq.com', 'expiry': 1598127679, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '77dhmkf'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '02142974'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'},
                   {'domain': '.work.weixin.qq.com', 'expiry': 1629632143, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'},
                   {'domain': '.work.weixin.qq.com', 'expiry': 1600688143, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}]
        db = shelve.open('db/loginCookies.db')
        db['cookie'] = cookies
        db.close()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_id('menu_contacts').click()

