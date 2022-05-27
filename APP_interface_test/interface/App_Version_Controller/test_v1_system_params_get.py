__author__ = 'huxm855'

import os

import requests


def test_v1_system_params(login):
    ''' 获取系统参数'''
    base_url = login[0] + "/v1/system/params"
    r = requests.get(base_url, headers=login[-1], verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
