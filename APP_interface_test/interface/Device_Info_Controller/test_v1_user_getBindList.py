__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import requests


def test_v1_user_getBindList(login, ):
    ''' 获取账号绑定列表'''
    base_url = login[0] + "/v1/user/getBindList"
    r = requests.get(base_url, headers=login[-1], verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
