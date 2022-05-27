__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import requests

from db_fixture.common import GlobalVar, Encrypt


@pytest.mark.parametrize('userId',['None',GlobalVar.GVar_hxm['user_id'],'hhly'])
@pytest.mark.parametrize('pwd',[None,Encrypt().md5Encode(GlobalVar.GVar_hxm['passworld']),'123'])
def test_v1_user_validatePWD(login,userId,pwd):
    ''' 验证密码'''
    base_url =login[0] + "/v1/user/validatePWD"
    params={'userId':userId,'pwd':pwd}
    r = requests.get(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    if userId==GlobalVar.GVar_hxm['user_id'] and pwd is not None:
        if pwd=='123':
            assert result['msg'] == '原密码错误'
        else:
            assert result['msg']==  '成功'
    else:
        assert result['result'] in ('2','4002')
#  AssertionError: assert '2103' in ('2', '4002')


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
