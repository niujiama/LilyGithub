import json

import requests
import yaml

class BaseAPIs:
    def load_apis(self):
        with open("../data/apis.yaml", encoding="utf-8") as f:
            apis = yaml.safe_load(f)
        return apis

    def load_radioList(self):
        with open("../data/radioList.yaml", encoding="utf-8") as f:
            radioLists = yaml.safe_load(f)
        x = len(radioLists)
        ids = []
        params = []
        for i in range(x):
            ids.append(radioLists[i]["ids"])
            params.append((radioLists[i]["params"], radioLists[i]["expected"]))
        return ids, params

    def load_audioList(self):
        with open("../data/audioList.yaml", encoding="utf-8") as f:
            audioLists = yaml.safe_load(f)
        x = len(audioLists)
        ids = []
        params = []
        for i in range(x):
            ids.append(audioLists[i]["ids"])
            params.append((audioLists[i]["params"], audioLists[i]["expected"]))
        return ids, params

    def k_request(self, method, url, params):
        r = requests.request(method=method, url=url, params=params)
        return r

    def k_assert(self, r, expected):
        if expected["method"] == "errcode":
            assert str(expected["value"]) == r.json()["errcode"]
        elif expected["method"] == "result":
            assert expected["value"] < r.json()["result"][0]["audioId"]
        else:
            print("暂未考虑的情况，请修改代码！")
        print(r.json())
