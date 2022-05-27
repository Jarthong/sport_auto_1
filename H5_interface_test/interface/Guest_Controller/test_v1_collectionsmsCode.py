#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests
from db_fixture.getdata import *

phone = [13133741005]
@pytest.mark.parametrize('phone',phone)
@pytest.mark.parametrize('operateType',[1])
def test_collectionSmsCode(login_hq3,phone,operateType):
    """
    收集用户信息获取验证码
    operateType == (1：手机注册，2：绑定手机，3：修改登录密码，4：忘记密码，5：修改绑定手机号码，7：组织用户信息认证，10：绑定银行卡短信验证码,11 :用户信息认证)
    :param public:
    :return:
    """
    base_url = login_hq3.host + "/v1/guest/collectionSmsCode"
    params = {
        'phone':phone,
        'operateType':operateType
    }
    print(params)
    r = requests.get(base_url, headers=login_hq3.headers, verify=False, params=params)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))







