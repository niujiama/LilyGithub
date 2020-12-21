import math
import os
import time
import requests

# os的使用：在b下创建test.txt
if not os.path.exists('b'):
    os.mkdir('b')
if not os.path.exists('b/test.txt'):
    with open('b/test.txt', 'w') as f:
        f.write('hello, os using')

# time的使用
print(time.asctime())   #国外的时间格式
print(time.time())  #时间戳
# time.sleep(2)   #等待2秒钟
print(time.localtime()) #时间戳转换成时间元组
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) #讲当前时间转换成带格式的时间
print(time.strftime("%Y年%m月%d日 %H时%M分%S秒", time.localtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S %A"))

# math的使用
x = 5.5
print(math.ceil(x))     #小数进位
print(math.floor(x))    #小数舍弃
print(math.sqrt(16))    #平方根




