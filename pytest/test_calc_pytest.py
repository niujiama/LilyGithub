import Calculator as Calculator
import pytest
import yaml

'''
课后作业：
1、补全计算器（加法 除法）的测试用例
2、使用参数化完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
注意：
使用等价类，边界值，因果图等设计测试用例
测试用例中添加断言，验证结果
灵活使用 setup(), teardown() , setup_class(), teardown_class()
'''

# 用yaml做数据驱动
def get_data():
    with open('./data/calc.yml', encoding='utf-8') as f:
        mydata = yaml.safe_load(f)
        addData = mydata['add']['data']
        addIds = mydata['add']['myids']
        addFloatData = mydata['add_float']['data']
        addFloatIds = mydata['add_float']['myids']
        divData = mydata['div']['data']
        divIds = mydata['div']['myids']
    return [addData, addIds, addFloatData, addFloatIds, divData, divIds]

# 计算类
class TestCalc:
    def setup_class(self):
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    #定义整数加法方法
    # @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect', get_data()[0], ids=get_data()[1])
    def test_add(self, a, b, expect):
        try:
            result = a + b
            print(f' 测试用例：{a}+{b}={result}')
            assert expect == result
        except:
            print('测试数据异常！请检查测试数据是否都为整数')
            raise ValueError

    #定义浮点数加法方法
    # @pytest.mark.add_float
    @pytest.mark.parametrize('a,b,expect', get_data()[2], ids=get_data()[3])
    def test_add_float(self, a, b, expect):
        try:
            result = round((a + b), 2)
            print(f' 测试用例：{a}+{b}={result}')
            assert expect == result
        except:
            print('测试数据异常！请检查测试数据是否都为浮点数')
            raise ValueError

    # @pytest.mark.div
    @pytest.mark.parametrize('a,b,expect', get_data()[4], ids=get_data()[5])
    def test_div(self, a, b, expect):
        try:
            result = round((a/b), 2)
            print(f' 测试用例：{a}//{b}={result}')
            assert expect == result
        except:
            print('测试数据异常！请检查测试数据是否都数值型，且除数不能为零')
            raise ValueError