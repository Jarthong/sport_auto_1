__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import requests


def test_v1_user_city_latestUserSchule(login):
    ''' 查询用户今日起最近的日程数据列表接口'''
    base_url = login[0] + "/v1/user/city/latestUserSchule"
    r = requests.get(base_url, headers=login[-1], verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
