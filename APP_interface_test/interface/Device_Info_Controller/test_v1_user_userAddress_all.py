from interface.Device_Info_Controller.data_fixture import Device_Info_Controller

__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import pytest
import re
import requests

from db_fixture.common import GlobalVar, RandomVar

rows=[1,10,50,100]
@pytest.mark.parametrize('rows',rows)
def test_v1_user_userAddress_get(login,rows):
    ''' 查询用户收货地址'''
    base_url =login[0] + "/v1/user/userAddress"
    params = {
              'page': 1,
              'rows': rows,
              }
    r = requests.get(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    assert result['data']['total']==Device_Info_Controller().user_delivery_address()[0]


userId=[GlobalVar.GVar_hxm['user_id']]
city =['10002',None]
detailAddress=['autotest详细地址'+RandomVar().random_char_upper(),None]
dist=['10003',None]
isDefaultAddress=[0,1]
mobile=[RandomVar().random_phone(),'1232']
prov=['10001',None]
@pytest.mark.parametrize('userId',userId)
@pytest.mark.parametrize('city',city)
@pytest.mark.parametrize('detailAddress',detailAddress)
@pytest.mark.parametrize('dist',dist)
@pytest.mark.parametrize('isDefaultAddress',isDefaultAddress)
@pytest.mark.parametrize('mobile',mobile)
@pytest.mark.parametrize('prov',prov)
def test_v1_user_userAddress_post(login,userId,city,detailAddress,dist,isDefaultAddress,mobile,prov):
    ''' 保存用户收货地址'''
    base_url = login[0] + "/v1/user/userAddress"
    params = {
        'city': city,
        'consignee': RandomVar().random_char_upper(),
        'detailAddress': detailAddress,
        'dist': dist,
        'isDefaultAddress': isDefaultAddress,
        'mobile': mobile,
        'prov': prov,
        'userId': userId
    }
    r = requests.post(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    if  city== None or dist==None or detailAddress==None or prov== None or mobile=='1232' :
        assert re.search('2|4002|13',str(result['result']))
    else:
        assert result['result'] == '0' or result['result'] == '2123'



userAddressId=[Device_Info_Controller().user_delivery_address(column='id')[0],None]
userId=[GlobalVar.GVar_hxm['user_id']]
city =['11959',None]
detailAddress=['autotest详细地址'+RandomVar().random_char_upper(),None]
dist=['11962',None]
isDefaultAddress=[0,1]
mobile=[RandomVar().random_phone(),'1232']
prov=['11935',None]

@pytest.mark.parametrize('userAddressId',[pytest.param(userAddressId[0], marks=pytest.mark.skipif(userAddressId[0]==0,reason='无收货地址，无法修改收货地址操作')),
                                          ]
                         )
@pytest.mark.parametrize('userId',userId)
@pytest.mark.parametrize('city',city)
@pytest.mark.parametrize('detailAddress',detailAddress)
@pytest.mark.parametrize('dist',dist)
@pytest.mark.parametrize('isDefaultAddress',isDefaultAddress)
@pytest.mark.parametrize('mobile',mobile)
@pytest.mark.parametrize('prov',prov)
def test_v1_user_userAddress_put(login,userId,city,detailAddress,dist,isDefaultAddress,mobile,prov,userAddressId):
    ''' 修改用户收货地址'''
    base_url = login[0] + "/v1/user/userAddress"
    params = {
        'id':userAddressId,
        'city': city,
        'consignee': RandomVar().random_char_upper(),
        'detailAddress': detailAddress,
        'dist': dist,
        'isDefaultAddress': isDefaultAddress,
        'mobile': mobile,
        'prov': prov,
        'userId': userId
    }
    r = requests.put(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    if mobile=='1232' :
        assert re.search('4002',str(result['result']))
    else:
        assert result['result'] == '0'



@pytest.mark.parametrize('userAddressId',[pytest.param(userAddressId[0], marks=pytest.mark.skipif(userAddressId[0]==0,reason='无收货地址，无法删除收货地址操作')),
                                          userAddressId[-1]
                                          ]
                         )
def test_v1_user_userAddress_delete(login,userAddressId):
    ''' 删除v'''
    base_url = login[0] + "/v1/user/userAddress"
    params = {
        'id':userAddressId
    }
    r = requests.delete(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    if userAddressId is None:
        assert result['result']=='4002'
    else:
        assert result['result'] == '0'



if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))


