# 测试某个字符串是不是包含在一个长字符串里，并且返回字符串的下标号
# ‘lily’，‘My name is lily.’
#
# subStr = 'lily'
# str1 = 'My name is lily.'
# subStrLen = len(subStr)
# str1Len = len(str1)
#
# for i in range(str1Len-subStrLen):
#     if str1[i:i+subStrLen]==subStr:
#         print(f'substr is in str1 and position starts at {i}')
#         break
# else:
#     print('substr is not in str1')

# 测试for-in，else
# for i in range(5):
#     print(i)
# else:
#     print('for循环正常结束')

# 测试while，else
# a = 0
# while a < 5:
#     print(a)
#     a += 1
# else:
#     print('while循环正常结束')

# 猜数字游戏
# 规则：机器随机出一个1~100的数字，人输入猜到的数字，程序根据输入数字提示大了小了，看人猜多少次能猜中。

import random

computer_num = random.randint(1, 100)
times = 0

while True:
    guess_num = int(input('请输入您猜测的1~100间的数字'))
    times += 1
    if guess_num == computer_num:
        print(f'您用了{times}次猜对了！')
        break
    elif guess_num > computer_num:
        print('猜的大了')
    elif guess_num < computer_num:
        print('猜的小了')

