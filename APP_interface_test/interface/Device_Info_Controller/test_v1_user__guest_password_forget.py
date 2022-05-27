# -*- coding: utf-8 -*-
__author__ = 'huxm855'
import os

import pytest
import requests
from db_fixture.common import GlobalVar

smsCode = ['666666', None]
phone = [GlobalVar.GVar_hxm['user_phone'], None]
newPassword = ['123456', None]


@pytest.mark.parametrize('smsCode', smsCode)
@pytest.mark.parametrize('phone', phone)
@pytest.mark.parametrize('newPassword', newPassword)
def test_v1_user__guest_password_forget(login, smsCode, phone, newPassword):
    ''' 忘记密码'''
    base_url = login[0] + "/v1/user/_guest/password/forget"
    params = {'phone': phone, 'smsCode': smsCode, 'newPassword': newPassword}
    r = requests.post(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)

    if smsCode == None or phone == None or newPassword == None:
        assert result['result'] in ['4002', '2']
        assert result['msg'] in ['手机号码格式不正确!', '对照接口文档,检查接口必输参数是否有值或参数类型是否正确...', '验证码输入不能为空!']
    else:
        assert result['result'] == '0' or result['result'] == '8'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
