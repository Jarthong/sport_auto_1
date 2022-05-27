__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import requests
from db_fixture.common import GlobalVar

accountType = list(range(1, 4))
operateType = list(range(1, 5))
country = list(range(0, 5))


@pytest.mark.parametrize('accountType', accountType)
@pytest.mark.parametrize('country', country)
@pytest.mark.parametrize('operateType', operateType)
def test_v1_user__guest_register(login, accountType, country, operateType):
    ''' 用户注册'''
    base_url = login[0] + "/v1/user/_guest/register"
    params = {'account': GlobalVar.GVar_hxm['user_phone'], 'loginPwd': GlobalVar.GVar_hxm['passworld'],
              'accountType': accountType, 'smsCode': '666666', 'country': country, 'inviteCode': '123456',
              'operateType': operateType}

    r = requests.post(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    assert result['result'] in ['4002', '1025']


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
