__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import requests


@pytest.mark.parametrize('thirdPartyType', range(1, 4))
def test_v1_user_bindThirdUser(login, thirdPartyType):
    ''' 绑定第三方用户'''
    base_url = login[0] + "/v1/user/bindThirdUser"
    params = {'thirdPartyType': thirdPartyType, 'thirdOpenId': '06E6ABF76D46C14233577ED61FBCD031',
              'token': '0E3077AB07987928A536B06D58628679'}
    r = requests.post(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] in ('成功', '第三方平台用户已经被绑定')


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
