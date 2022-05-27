__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import requests
from interface.Device_Info_Controller.data_fixture import Device_Info_Controller


@pytest.mark.parametrize('followUserId', [None, Device_Info_Controller().user_follow(column='followed_user_id')])
def test_v1_user_aliasName(login, followUserId):
    ''' 修改被关注的用户别称'''
    base_url = login[0] + "/v1/user/aliasName"
    params = {'followUserId': followUserId}
    r = requests.put(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    if followUserId == None:
        assert result['result'] == '4002'
    else:
        assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
