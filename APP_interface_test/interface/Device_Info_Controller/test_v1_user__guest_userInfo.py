__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import requests
from db_fixture.common import GlobalVar

userId = ['None', GlobalVar.GVar_hxm['user_id'], 'hhly']


@pytest.mark.parametrize('userId', userId)
def test_v1_user__guest_userInfo(login, userId):
    ''' 用户信息'''
    base_url = login[0] + "/v1/user/_guest/userInfo"
    params = {'userId': userId}
    r = requests.get(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    if userId == GlobalVar.GVar_hxm['user_id']:
        assert result['msg'] == '成功'
        assert result['data']['userId'] == userId
    else:
        assert result['msg'] == '用户不存在'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
