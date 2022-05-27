import pytest

__author__ = 'huxm855'
import os
import requests


@pytest.mark.parametrize('state', [None, '3fdc2d85e62040d18b3bb6d356c82ea8'])
# 在真实环境才会调用
def test_v1_user__guest_openid_wechat(login, state):
    '''微信平台登录回调，需要特殊处理result=2114(用户取消或禁止使用第三方平台账号登录)的结果'''
    base_url = login.host + "/v1/user/_guest/openid/wechat"
    params = {'state': state}
    r = requests.get(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    if state == None:

        assert result['msg'] == '参数错误[String@state]'
    else:
        assert result['result'] == '2116'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
