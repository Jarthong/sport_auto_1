__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import requests
from interface.Device_Info_Controller.data_fixture import Device_Info_Controller


@pytest.mark.parametrize('followUserId', [None, Device_Info_Controller().user_follow(column='followed_user_id')[0]])
def test_v1_user_isFollowed(login, followUserId):
    ''' 会员是否关注了followUserId'''
    base_url = login[0] + "/v1/user/isFollowed"
    params = {'followUserId': followUserId}
    r = requests.get(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    if followUserId == 0:
        assert result['data']['followResult'] == False
    elif followUserId == None:
        assert result['result'] == '4002'
    else:
        assert result['data']['followResult'] == True


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
