import pytest

__author__ = 'huxm855'

import os

import requests



@pytest.mark.parametrize('thirdType', list(range(1, 4)))
@pytest.mark.parametrize('deviceType', list(range(1, 7)))
def test_v1_user__guest_openid_login(login, thirdType, deviceType):
    ''' 请求第三方平台登录'''
    base_url = login.host + "/v1/user/_guest/openid/login"
    params = {'thirdType': thirdType, 'deviceType': deviceType,'callBackUrl':'hhlysport.com'}
    r = requests.get(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'
    assert result['data']['thirdType'] == thirdType
    assert result['data']['deviceType'] == deviceType
    assert result['data']['appId'] is not None


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
