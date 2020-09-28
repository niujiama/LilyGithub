import requests
import jsonschema


class TestOnly:
    def test_head(self):
        r = requests.head("http://httpbin.testing-studio.com/get")
        print(r.headers)

    def test_options(self):
        r = requests.options("http://httpbin.testing-studio.com/get")
        print(r.url)

    def test_get(self):
        url = "http://httpbin.testing-studio.com/get"
        # header = {'user-agent': 'my-app/0.0.3'}
        # r = requests.get(url, headers=header)
        r = requests.get(url)
        print(r.json())