#F-string方法
name = "Lily"
age = 20
list1 = ['Jone', 'Lucy', 'Marry']
dic1 = {'name': 'Tom', 'gender': 'male'}
print(f'my name is {name}, age is {age}')
print(f'my list is {list1}, dic is {dic1}')
# 列表可以直接读取元素
print(f'we name are {list1[0]}, {list1[1]} and {list1[2]}')
#字典可以直接调用
print(f'my name is {dic1["name"]}, gender is {dic1["gender"]}')
#还可以写使用函数/方法，只要不出现/就行
print(f'my upper name is {name.upper()}')