import requests


class BaseApi:

    def send_api(self, data: dict):
        """
        发送api
        """
        # print(json.dumps(data, indent=2))
        return requests.request(**data).json()