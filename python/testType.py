#定义变量，且不用指定类型--动态数据类型
int_a = 1
float_a = 0.5
complex_a = 0.2j
print(type(int_a))
print(type(float_a))
print(type(complex_a))
print('-------------digit------------------')

#字符串类型
str1 = 'abcdefgh'
str2 = '12345678'
print(str1 + str2)
print(str1[-2:])
print('-------------string------------------')

#列表类型
list1 = ['lily', 'shan', 'niuniu', 'jiajia']
list1.append('mama')
print(list1)
list1.insert(2, 'baba')
print(list1)
print(list1.count('shan'))
print('-------------list------------------')


#类型转换
ftoi = int(float_a)
itof = float(int_a)
itos = str(int_a)
stol = list(str1)
print(ftoi, type(ftoi))
print(itof, type(itof))
print(itos, type(itos))
print(stol, type(stol))