# 创建一个人类
# 通过class关键字定义了一个类
class Person():
    # 类变量，是通过类来访问 Person.name
    name = 'default'
    age = 0
    gender = 'male'
    weight = 0

    def __init__(self, name, age, gender, weight):
        # self.访问到的变量，必须用实例来访问 zs.name
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    def eat(self):
        print(f'{self.name} is eating')

    def play(self):
        print(f'{self.name} is playing')

    def jump(self):
        print(f'{self.name} is jumping')

zs = Person('zhangsan', 18, 'male', 130)
lisi = Person('lisi', 28, 'male', 140)
zs.eat()
lisi.eat()