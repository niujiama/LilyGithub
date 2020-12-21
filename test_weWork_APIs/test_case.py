import requests

class TestCases():
    def test_get(self):
        r = requests.get("http://httpbin.testing-studio.com/get")
        print(r.status_code)

        assert r.status_code == 200

    def test_post(self):
        r = requests.post("http://httpbin.testing-studio.com/post")
        print(r.status_code)

        assert r.status_code == 200

    def test_json(self):
        r = requests.get("https://ceshiren.com/categories.json")
        print(r.json())

        assert r.json()['category_list']['categories'][0]['name'] == '社区治理' and r.json()['category_list']['categories'][0]['color'] == '0088CC'
