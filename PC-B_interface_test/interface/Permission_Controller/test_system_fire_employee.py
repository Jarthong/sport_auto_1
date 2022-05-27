__author__ = 'huxm855'

import os
import re

import pytest
import requests

from db_fixture.common import GlobalVar
from interface.Permission_Controller.data_fixture import get_EmployeeId, get_UnemployeeId

userId = [get_EmployeeId(column='user_id'),
          get_EmployeeId(column='user_id', user_id=GlobalVar.GVar['train_org_userId']), get_UnemployeeId()]
authOrgId = GlobalVar.GVar['authOrgIds'] + [GlobalVar.GVar['match_org_userId']]
type = range(1, 4)


@pytest.mark.parametrize('userId,authOrgId,type', list(zip(userId, authOrgId, type)))
def test_system_fire_employee(login, userId, authOrgId, type):
    '''员工IP-赛事组织 解除关系'''
    base_url = login.host + '/system/fire/employee'
    params = {
        'userId': userId,
        'authOrgId': authOrgId
    }
    r = requests.post(base_url, headers=login.headers, params=params)
    result = r.json()
    print(result)
    if type != 3:
        assert result['result'] == '0'
        re.search('成功', str(result))
    else:
        assert result['result'] == '3009'
        re.search('用户还不是队员或者没有权限 操作成员数据', str(result))


if __name__ == '__main__':
    pytest.main(['-s','-v',__file__])
