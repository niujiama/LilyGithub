import base64
import json
import requests
import yaml

"""
1. 在一个用例中实现，数据定义、接口调用、返回值解密这3个步骤。
2. 把数据和接口分离，构造一层通用的send方法，放到一个py中；测试用例调用send，放到另外的py中。
   传入的环境信息，直接写在测试用例py中。
3. 传入的环境信息，url可以替换成ip。使用场景：正式环境、测试环境切换
4. 传入的环境信息，可以单独放到yaml文件中，实现配置文件和源代码的分离
"""

class RequestAPIs:
    env = yaml.safe_load(open("env_config.yaml"))

    def send(self, data: dict):
        data["url"] = str(data["url"]).replace("testing-studio", self.env["hosts"][self.env["default"]])
        print(data["url"])
        if "http" == data["schema"]:
            res = requests.request(data["method"], data["url"], headers=data["headers"])
            return json.loads(base64.b64decode(res.content))
        elif "dubbo" == data["schema"]:
            pass
        elif "websocket" == data["schema"]:
            pass