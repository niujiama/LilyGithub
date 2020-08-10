
class Bicycle():
    def run(self, km):
        print('骑行了{km}千米')

class EBicycle(Bicycle):
    # 需要初始化变量的话，可以放到构造函数里
    def __init__(self, valume):
        self.valume = valume
