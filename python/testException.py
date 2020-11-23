#使用系统异常
try:
    num1 = int(input("请输入一个除数："))
    num2 = int(input("请输入一个被除数："))
    print((num1 / num2))
except:
    print('这是一个万能异常！')
else:
    print('不发生异常，会执行！')
finally:
    print('发生或者没发生异常，都会执行这里！')

# # #自己抛出异常
# x = 10
# if x > 5:
#     raise Exception('这是一个自己抛出的异常！')

# 自己定义异常类
class MyException(Exception):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

raise MyException(1, 2)