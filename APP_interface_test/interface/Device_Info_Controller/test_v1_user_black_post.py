# -*- coding: utf-8 -*-
import os
import random

import pytest
import requests
from interface.Device_Info_Controller.data_fixture import Device_Info_Controller


# bug 可添加登录用户 seedp50 为黑名单
@pytest.mark.parametrize('blackUserId',
                         [None, random.choice(Device_Info_Controller().user_info('user_id', on='!=')), 'hhly'])
def test_v1_user_black(login, blackUserId):
    ''' 加入黑名单'''
    base_url = login[0] + "/v1/user/black"
    params = {'blackUserId': blackUserId}
    r = requests.post(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    if blackUserId is None:

        assert result['result'] == '4002'
    elif blackUserId == 'hhly':
        assert result['msg'] == '用户不存在'
    else:
        assert result['msg'] in ('黑名单人员已经存在', '成功')


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
