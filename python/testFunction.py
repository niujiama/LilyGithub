def func1(a=5, b=2):
    c = a+b
    return c

result=func1(1,2)
print('function', result)


func2 = lambda x, y: x+y
print('lambda', func2(3, 4))