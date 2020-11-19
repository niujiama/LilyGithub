def setup_module():
    print("Setup Module---------1")

def teardown_module():
    print("Teardown Module---------1")

class TestModule1:
    @classmethod
    def setup_class(cls):
        print("Setup Class---------2")

    @classmethod
    def teardown_class(cls):
        print("Teardown Class---------2")

    def setup_method(self):
        print("Setup Method---------3")

    def teardown_method(self):
        print("Teardown method---------3")

    def test_method1(self):
        print("this is test_method1")

    def test_method2(self):
        print("this is test_method2")

    def test_method3(self):
        print("this is test_method3")

class TestModule2:
    def test_method4(self):
        print("this is test_method4")

    def test_method5(self):
        print("this is test_method5")

    def test_method6(self):
        print("this is test_method6")