import json
import os

import pytest
import yaml

from test_KradioBasic.base_api import BaseApi

def read_yaml(path):
    with open(path, 'r', encoding='utf8') as f:
        return yaml.safe_load(f.read())

class Test_cases():  #注意：测试类不能继承BaseApi这种类
    # 定义一个baseapi的对象，让测试类使用
    base = BaseApi()
    yml_file_path = os.path.join(base.BASE_PATH, "test_KradioBasic/testdata.yml")

    # @pytest.mark.parametrize('data, expected', [({'url':'http://open.kaolafm.com/v2/radio/list?rid=1200000000099&clockid=&packagename=com&carType=aio_3m_otfp&sign=7350a61333bc65d644a66bbd4c20d5fb&sdkversion=1.5.5&version=2.7.0.0001&appid=ye8192&udid=799151406a36cd306ac381036dca852b&deviceid=799151406a36cd306ac381036dca852b&lat=39.985405&channel=ceshizhuanyong_kradio&lng=116.304996&os=android&openid=ye81922020042410009258',
    #                                    'method':'get'}, '新闻电台'),
    #                                             ({'url':'http://open.kaolafm.com/v2/album/detail?ids=1100000036391&packagename=com.edog.car.ceshizhuanyong_kradio&carType=aio_3m_otfp&sign=7350a61333bc65d644a66bbd4c20d5fb&sdkversion=1.5.5&version=2.7.0.0001&appid=ye8192&udid=799151406a36cd306ac381036dca852b&deviceid=799151406a36cd306ac381036dca852b&lat=39.985892&channel=ceshizhuanyong_kradio&lng=116.305035&os=android&openid=ye81922020042410009258',
    #                                    'method':'get'}, '十点读书')])
    # @pytest.mark.parametrize('data, expected', read_yaml('./testdata.yml'))
    @pytest.mark.parametrize('data, expected', read_yaml(yml_file_path))
    def test_apis(self, data, expected):
        r = self.base.send_api(data)
        resStr = json.dumps(r, ensure_ascii=False)  #不适用Ascii码格式，一般就能正常显示中文了
        print(resStr)
        assert expected in resStr

