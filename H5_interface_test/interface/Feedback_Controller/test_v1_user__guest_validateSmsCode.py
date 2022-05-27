import os

import pytest

from db_fixture.common import GlobalVar

__author__ = 'huxm855'

import requests


@pytest.mark.parametrize('operateType', [x for x in range(1, 6)] + [7, 10, 11])
@pytest.mark.parametrize('smsCode', ['666666', None])
def test_v1_user__guest_validateSmsCode(login, operateType, smsCode):
    ''' 验证验证码'''
    base_url = login.host + "/v1/user/_guest/validateSmsCode"
    params = {'operateType': operateType, 'validateMsg': smsCode, 'somethingStr': GlobalVar().GVar['user_phone'],
              'validateType': 5}
    r = requests.get(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    if smsCode != None:
        assert result['msg'] in ('验证码已失效', '验证码已失效，开发环境请输入：666666', '成功')
    else:
        assert result['msg'] in ('smsCode不能为空！')


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
