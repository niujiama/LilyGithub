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
# def get_data():
#     with open('./data/calc.yml', encoding='utf-8') as f:
#         mydata = yaml.safe_load(f)
#         adddata = mydata['add']['data']
#         myids = mydata['add']['myids']
#     return [adddata, myids]

#计算类
class TestCalc:
    def setup_class(self):
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect', [
        (1, 1, 2),
        (100, 200, 300),
        ('a', 'b', 'ab'),
        (0.1, 0.2, 0.3),
        (-1, -2, -3)
    ])
    # @pytest.mark.parametrize('a,b,expect', )
    def test_add(self, a, b, expect):
        '''
        测试相加
        '''
        print("测试相加")
        result = a + b
        assert expect == result

    @pytest.mark.parametrize('a,b,expect', [
        (0.1, 0.1, 0.2),
        (0.1, 0.2, 0.3)
    ])
    def test_add_float(self, a, b, expect):
        result = round((a + b), 2)
        assert expect == result

    @pytest.mark.parametrize('a,b,expect', [
        (1, 1, 1),
        (2, 1, 2),
        (5, 2.5, 2),
        (1, 2, 0.5),
        (1, 0, 0),
        (0, 1, 0),
        (1, 2, 5),
        ('a', 'b', 'c')
    ])
    def test_div(self, a, b, expect):
        try:
            result = (a/b)
            assert expect == result
        except (ZeroDivisionError, TypeError) as err:
            raise ValueError

