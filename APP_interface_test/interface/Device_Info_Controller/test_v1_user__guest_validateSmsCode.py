__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import requests
from db_fixture.common import GlobalVar


@pytest.mark.parametrize('operateType',[x for x in range(1, 6)] + [7, 10])
@pytest.mark.parametrize('validateMsg',[None,'666666'])

def test_v1_user__guest_validateSmsCode(login,operateType,validateMsg):
    ''' 验证验证码'''
    base_url =login[0] + "/v1/user/_guest/validateSmsCode"
    params={'operateType':operateType,'validateMsg':validateMsg,'somethingStr':GlobalVar().GVar_hxm['user_phone'],'validateType':5}
    r = requests.get(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    if validateMsg != None:
        assert result['msg']in ('验证码已失效，开发环境请输入：666666','成功')
    else:
        assert result['msg']in ('smsCode不能为空！')

if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
