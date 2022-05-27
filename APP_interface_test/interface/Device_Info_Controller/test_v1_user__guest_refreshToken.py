__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import time

import pytest
import requests
from db_fixture.common import GlobalVar

tokenTime = [None, str(int(time.time() * 1000))]


@pytest.mark.parametrize('tokenTime', tokenTime, ids=tokenTime)
def test_v1_user__guest_refreshToken(login, tokenTime):
    ''' 刷新token'''
    base_url = login[0] + "/v1/user/_guest/refreshToken"
    params = {'userId': GlobalVar.GVar_hxm['user_id'], 'tokenTime': tokenTime, 'signature': login[-1]['X-SNS-Signature']}
    r = requests.post(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] in ['tokenTime输入不正确!', '签名错误']


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
