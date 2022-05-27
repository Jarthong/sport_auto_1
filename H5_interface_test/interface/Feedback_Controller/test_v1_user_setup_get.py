from db_fixture.common import GlobalVar

__author__ = 'huxm855'

import os

import requests


def test_v1_user_setup(login):
    ''' 获取用户隐私信息设置'''
    base_url = login.host + "/v1/user/setup"
    r = requests.get(base_url, headers=login.headers, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'
    assert result['data']['userId'] == GlobalVar.GVar['user_id']


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
