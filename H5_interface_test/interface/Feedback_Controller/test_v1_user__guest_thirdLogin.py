__author__ = 'huxm855'

import os

import pytest
import requests


@pytest.mark.parametrize('thirdPartyType', range(1, 4))
def test_v1_user__guest_thirdLogin(login, thirdPartyType):
    ''' 用户登录(第三方)'''
    base_url = login.host + "/v1/user/_guest/thirdLogin"
    params = {'thirdPartyType': thirdPartyType, 'thirdOpenId': '06E6ABF76D46C14233577ED61FBCD031',
              'token': '0E3077AB07987928A536B06D58628679'}
    r = requests.post(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
