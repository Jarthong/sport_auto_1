__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import requests
from db_fixture.common import GlobalVar

androidDeviceToken = [None, '12345']
iosDeviceToken = [None, '12345']


@pytest.mark.parametrize('cateCode', androidDeviceToken, ids=iosDeviceToken)
def test_v1_user__guest_refreshUMToken(login, cateCode):
    ''' 刷新友盟token'''
    base_url = login[0] + "/v1/user/_guest/refreshUMToken"
    params = {'androidDeviceToken': androidDeviceToken, 'iosDeviceToken': iosDeviceToken,
              'userId': GlobalVar.GVar_hxm['user_id']}

    r = requests.post(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
