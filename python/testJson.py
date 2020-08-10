import json
#Json是由字典和列表组成的
data = {
    'name': 'lily',
    'age': 20,
    'gender': 'female'
}
print(data)
print(type(data))
#把json转换成str类型
data1 = json.dumps(data)
print(data1)
print(type(data1))
# 把str类型转换成json类型
data2 = json.loads(data1)
print(data2)
print(type(data2))