__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import requests
from db_fixture.common import GlobalVar

phone = [GlobalVar.GVar_hxm['user_phone'], None]
# 操作类型(1：手机注册，2：绑定手机，3：修改登录密码，4：忘记密码，5：修改绑定手机号码，7：组织用户信息认证，10：绑定银行卡短信验证码,11 :用户信息认证)
operateType = [x for x in range(1, 6)] + [7, 10, 11]
validateCode = ['666666', None]


@pytest.mark.parametrize('phone', phone)
@pytest.mark.parametrize('operateType', operateType)
@pytest.mark.parametrize('validateCode', validateCode)
def test_v1_user__guest_smsCode(login, phone, operateType, validateCode):
    ''' 获取验证码'''
    base_url = login[0] + "/v1/user/_guest/smsCode"
    params = {'phone': phone, 'operateType': operateType, 'validateCode': validateCode}

    r = requests.get(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] in ['用户已经存在', '手机号码格式不正确!','请求太频繁，请稍后再试！']


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
