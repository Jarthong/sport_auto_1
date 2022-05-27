import pytest

__author__ = 'huxm855'

import os

import requests

from db_fixture.common import GlobalVar


@pytest.mark.parametrize('userId', ['None', GlobalVar.GVar['user_id'], 'hhly'])
def test_v1_user__guest_userInfo(login, userId):
    ''' 用户信息'''
    base_url = login.host + "/v1/user/_guest/userInfo"
    params = {'userId': userId}
    r = requests.get(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    if userId == GlobalVar.GVar['user_id']:
        assert result['msg'] == '成功'
        assert result['data']['userId'] == userId
    else:
        assert result['msg'] == '用户不存在'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
