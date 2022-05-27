#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests
from db_fixture.common import *
from db_fixture.getdata import *

count = (GetData('count(*)','user_info a,train_teacher b,biz_sensitive c',
                "a.user_id = b.created_id and b.SID = c.ID and a.phone = {phone} and b.`status` = {status}"
                .format(phone=GlobalVar.GVar_hq['user_phone2'],status=1)).result())
name1= (GetData('c.user_name','user_info a,train_teacher b,biz_sensitive c',
                "a.user_id = b.created_id and b.SID = c.ID and a.phone = {phone} and b.`status` = {status}"
                .format(phone=GlobalVar.GVar_hq['user_phone2'],status=1)).result())
name = [name1,None,'%^&']
@pytest.mark.parametrize('name',name)
def test_teacher_list(login_hq2,name):
    """
    分页获取教练信息
    :param public:
    :return:
    """
    base_url = login_hq2.host + "/train/teacher/list"
    params = {
        'name':name,
        'provinceId':None,
        'cityId':None,
        'order':'ASC',
        'page':1,
        'rows':15
    }
    print(params)
    r = requests.get(base_url, headers=login_hq2.headers, verify=False, params=params)
    result = r.json()
    print(result)
    if params == None:
        assert result['data']['total'] == count
        assert result['data']['msg'] == '成功'
        assert name1 in  result['data']['list']['name']
    elif params == name1:
        assert name1 in result['data']['list']['name']
    elif params == '%^&':
        assert result['data']['msg'] == '成功'



if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))








