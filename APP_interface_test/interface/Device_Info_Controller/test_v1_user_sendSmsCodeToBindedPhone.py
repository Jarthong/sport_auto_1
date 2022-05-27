__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import pytest
import requests


@pytest.mark.parametrize('operateType',[8,9])

def test_v1_user_sendSmsCodeToBindedPhone(login,operateType):
    ''' 发送短信验证码到已绑定手机'''
    base_url =login[0] + "/v1/user/sendSmsCodeToBindedPhone"
    params={'operateType':operateType}
    r = requests.get(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    assert result['msg']==  '成功' or  result['msg']==  '请求太频繁，请稍后再试！'
    


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
