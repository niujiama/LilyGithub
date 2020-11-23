import json
import os

import requests

class BaseApi:
    # 定义一个base_path，也就是项目的绝对路径，比如项目的路径是c：\api_test，不管放到哪儿，比如放到d盘，绝对路径都不会改变
    # 定义绝对路径，固定写法，适合于二级目录，三级目录就外套os.path.dirname
    # 后续在if __name__ 测试好啦
    BASE_PATH=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    """
    api 的抽象类
    """
    def send_api(self, data: dict):
        """
        发送 api
        """
        # print(json.dumps(data, indent=2))
        return requests.request(**data).json()

# if __name__=="__main__":
#     print(BaseApi().BASE_PATH)