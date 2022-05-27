__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import pytest
import requests

from db_fixture.common import GlobalVar, Encrypt, RandomVar


@pytest.mark.parametrize('smsCode',[None,'666666'])
@pytest.mark.parametrize('userId',['None',GlobalVar.GVar_hxm['user_id'],'hhly'])
@pytest.mark.parametrize('phone',[GlobalVar.GVar_hxm['user_phone'],RandomVar().random_phone(),None])
@pytest.mark.parametrize('operateType',[2,5])
@pytest.mark.parametrize('password',[None,Encrypt().md5Encode(GlobalVar.GVar_hxm['passworld']),'123'])

def test_user_updPhone(login,userId,smsCode,phone,operateType,password):
    ''' 绑定'''
    base_url =login[0] + "/v1/user/updPhone"
    params={'userId': userId, 'phone': phone, 'smsCode':smsCode, 'operateType': operateType, 'newPassword': password}
    r = requests.post(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    if smsCode==None:
        assert result['result']=='4002'or result['result']=='2103'
    elif userId==None:
        assert result['result']=='13'


    


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
