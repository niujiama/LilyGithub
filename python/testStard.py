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
print(time.asctime())
print(time.time())
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


