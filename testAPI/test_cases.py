from testAPI.APIs import RequestAPIs


class TestCases:
    def test_base64(self):
        data = {
            "schema": "http",
            "method": "get",
            "url": "http://testing-studio:9999/base64.txt",
            "headers": None
        }
        r = RequestAPIs()
        decodeJson = r.send(data)
        print(decodeJson)
        assert decodeJson["topics"]["president"] == "seveniruby"