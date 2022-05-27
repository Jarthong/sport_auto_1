import pytest

from db_fixture.common import GlobalVar

__author__ = 'huxm855'
import os

import requests



@pytest.mark.parametrize('phone', [GlobalVar.GVar['user_phone'], '13628592308', None])

# 操作类型(1：手机注册，2：绑定手机，3：修改登录密码，4：忘记密码，5：修改绑定手机号码，7：组织用户信息认证，10：绑定银行卡短信验证码,11 :用户信息认证)
@pytest.mark.parametrize('operateType', [x for x in range(1, 6)] + [7, 10, 11])
@pytest.mark.parametrize('smsCode', ['666666', None])
def test_v1_user__guest_smsCode(login, phone, operateType, smsCode):
    ''' 获取验证码'''
    base_url = login.host + "/v1/user/_guest/smsCode"
    params = {'phone': phone, 'operateType': operateType, 'validateCode': smsCode}

    r = requests.get(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    assert result['result'] in ['0', '2', '25', '9', '1025', '4002']


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
