import pytest
import requests
import json


class TestMutiParas:
    #传入正常类型的参数
    @pytest.mark.parametrize("a, b", [{1, 2}, {"a", "b"}, {5, 6}], ids=["case1", "case2", "case3"])
    def test_foo1(self, a, b):
        print(f"this is {a}, {b}")

    @pytest.mark.parametrize("a, d", [("a", "d")])
    @pytest.mark.parametrize("b, c", [(1, {"o": 1}), (2, "y"), (3, "z")])
    def test_foo2_1(self, a, d, b, c):
        print(f"this is a:{a}, d:{d}, b:{b}, c:{c}")

    @pytest.mark.parametrize("a, d", [{"a", "d"}])
    @pytest.mark.parametrize("b", [1, 2, 3])
    @pytest.mark.parametrize("c", ["x", "y", "z"])
    def test_foo2_2(self, a, d, b, c):
        print(f"this is a:{a}, d:{d}, b:{b}, c:{c}")

    def test_foo3(self):
        x = "{'a': 1, 'b': 2}"
        print(type(x))
        y = eval(x)
        print(type(y))

    @pytest.mark.parametrize("method, url", [("get", "http://open.kaolafm.com/v2/radio/list")])
    @pytest.mark.parametrize("expected, params", [({"method": "result", "value": 100}, {
        "rid": 1200000000099,
        "clockid": 0,
        "packagename": "com.edog.car.ceshizhuanyong_kradio",
        "carType": "aio_3m_otfp",
        "sign": "7350a61333bc65d644a66bbd4c20d5fb",
        "sdkversion": "1.5.5",
        "version": "2.7.1.0001",
        "appid": "ye8192",
        "udid": "799151406a36cd306ac381036dca852b",
        "deviceid": "799151406a36cd306ac381036dca852b",
        "lat": 39.985405,
        "channel": "ceshizhuanyong_kradio",
        "lng": 116.304996,
        "os": "android",
        "openid": "ye81922020042410009258"
    })])
    def test_foo5(self, method, url, expected, params):
        r = requests.request(method=method, url=url, params=params)
        if expected["method"] == "errcode":
            assert expected["value"] == r.json()["errcode"]
        elif expected["method"] == "result":
            assert expected["value"] < r.json()["result"][0]["audioId"]
        else:
            print("暂未考虑的情况，请修改代码！")