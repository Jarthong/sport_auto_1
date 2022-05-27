__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import pytest
import requests


@pytest.mark.parametrize('smsCode',[None,'666666'])
@pytest.mark.parametrize('operateType',[8,9,None])

def test_v1_user_validateSmsCodeForBindedPhone(login,smsCode,operateType):
    ''' 验证已绑定手机的验证码'''
    base_url =login[0] + "/v1/user/validateSmsCodeForBindedPhone"
    params={'smsCode':smsCode,'operateType':operateType}
    r = requests.get(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    if operateType !=None and smsCode !=None:
        assert result['result'] in ('6','8','0')
    else:
        assert result['result']==  '4002'

    


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
