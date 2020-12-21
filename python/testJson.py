import json
#Json是由字典和列表组成的
data = {
    'name': 'lily',
    'age': 20,
    'gender': 'female'
}
print(data)
print(type(data))
#将 Python 对象编码成 JSON 字符串
data1 = json.dumps(data)
print(data1)
print(type(data1))
# 将已编码的 JSON 字符串解码为 Python 对象
data2 = json.loads(data1)
print(data2)
print(type(data2))