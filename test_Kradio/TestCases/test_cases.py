import pytest

from test_Kradio.APIs.baseAPIs import BaseAPIs

class TestCases:
    base = BaseAPIs()
    rIds = base.load_radioList()[0]
    rParams = base.load_radioList()[1]
    aIds = base.load_audioList()[0]
    aParams = base.load_audioList()[1]

    @pytest.mark.parametrize("params, expected", rParams, ids=rIds)
    def test_radio_list(self, params, expected):
        method = self.base.load_apis()["radioList"]["method"]
        url = self.base.load_apis()["radioList"]["url"]
        r = self.base.k_request(method=method, url=url, params=params)
        if expected["method"] == "errcode":
            assert str(expected["value"]) == r.json()["errcode"]
        elif expected["method"] == "result":
            assert expected["value"] < r.json()["result"][0]["audioId"]
        else:
            print("暂未考虑的情况，请修改代码！")
        print(r.json())

    @pytest.mark.parametrize("params, expected", aParams, ids=aIds)
    def test_audio_list(self, params, expected):
        method = self.base.load_apis()["audioList"]["method"]
        url = self.base.load_apis()["audioList"]["url"]
        print(params)
        print(expected)
        r = self.base.k_request(method=method, url=url, params=params)
        if expected["method"] == "errcode":
            assert str(expected["value"]) == r.json()["errcode"]
        elif expected["method"] == "result":
            assert expected["value"] == r.json()["result"]["pageSize"]
        else:
            print("暂未考虑的情况，请修改代码！")
        print(r.json())

