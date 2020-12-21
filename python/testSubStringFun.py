#此方法主要检测：obj_str在test_str中出现了几次？在什么位置出现的？

obj_str = 'hello'
test_str = 'hello world, hello python'
obj_len = len(obj_str)
test_len = len(test_str)
count = 0
index = []
for i in range(test_len):
    if test_str[i:obj_len+i] == obj_str:
        print(test_str[i:obj_len+i])
        count = count
        index.append(i)

if count == 0:
    print(f'{obj_str} is not in {test_str}!')
else:
    print(f'{obj_str} is in {test_str}! It displays {count} times, places in {index}')