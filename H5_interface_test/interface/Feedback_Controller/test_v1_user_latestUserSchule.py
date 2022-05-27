__author__ = 'huxm855'

import os

import requests


def test_v1_user_latestUserSchule(login):
    ''' 查询用户今日起最近的日程数据列表接口'''
    base_url = login.host + "/v1/user/latestUserSchule"
    r = requests.get(base_url, headers=login.headers, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
