__author__ = 'huxm855'
import os

import requests


def test_v1_user__logout(login):
    ''' 退出登录'''
    base_url = login.host + "/v1/user/_logout"
    r = requests.post(base_url, headers=login.headers, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
