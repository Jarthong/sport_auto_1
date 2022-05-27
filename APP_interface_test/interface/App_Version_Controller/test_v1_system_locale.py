__author__ = 'huxm855'
import os
import requests


def test_v1_system_locale(login):
    ''' 根据 商品code 获取商品列表'''
    base_url = login[0] + "/v1/system/locale"
    r = requests.get(base_url, headers=login[-1],verify=False)
    result = r.json()
    print(result)
    assert result['title'] == 'CampusSports'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))