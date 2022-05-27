__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import requests
from interface.Device_Info_Controller.data_fixture import Device_Info_Controller


@pytest.mark.parametrize('followUserId',[None,Device_Info_Controller().user_follow(column='followed_user_id')])

def test_v1_user_friend(login,followUserId):
    ''' 新增关注'''
    base_url =login[0] + "/v1/user/friend"
    params={'followUserId':followUserId}
    r = requests.post(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    if followUserId == None:
        assert result['result'] == '4002'
    else:
        assert result['msg'] in('关注的用户不存在','成功')
    


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
