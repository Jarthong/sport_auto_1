__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import requests


@pytest.mark.parametrize('thirdPartyType', range(1, 4))
def test_v1_user__guest_thirdLogin(login, thirdPartyType):
    ''' 用户登录(第三方)'''
    base_url = login[0] + "/v1/user/_guest/thirdLogin"
    if thirdPartyType == 1:
        params = {'thirdPartyType': thirdPartyType, 'thirdOpenId': '31C325D1CF920B1B2CB6A0AC050435B0',
                  'token': '5B69CCA92014A07C9C8375ADBFAE553D', 'thirdUserIconUrl':'https://thirdqq.qlogo.cn/qqapp/1106109886/31C325D1CF920B1B2CB6A0AC050435B0/100'}
    else:
        params = {'thirdPartyType': thirdPartyType, 'thirdOpenId': '06E6ABF76D46C14233577ED61FBCD031',
                  'token': '0E3077AB07987928A536B06D58628679'}
    r = requests.post(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
