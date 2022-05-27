__author__ = 'huxm855'

import re

import pytest
import requests

from db_fixture.common import GlobalVar
from interface.Permission_Controller.data_fixture import get_EmployeeId, get_emplo_roleId

userId = [get_EmployeeId(column='user_id'),
          get_EmployeeId(column='user_id', user_id=GlobalVar().GVar['train_org_userId']),
          GlobalVar.GVar['match_org_userId'], ]
authOrgId = GlobalVar.GVar['authOrgIds'] + [GlobalVar.GVar['train_org_userId'], ]
roleId = [get_emplo_roleId(), get_emplo_roleId(group_user_id=GlobalVar().GVar['train_org_userId'], ip_cate_id='201'),
          get_emplo_roleId()]


@pytest.mark.parametrize('userId,authOrgId,roleId', list(zip(userId, authOrgId, roleId)))
def test_system_bind_role(login, userId, authOrgId, roleId):
    base_url = login.host + '/system/bind/role'
    params = {
        'userId': userId,
        'authOrgId': authOrgId,
        'roleId': roleId,
    }

    r = requests.post(base_url, headers=login.headers, params=params)
    result = r.json()
    print(result, params)
    if userId==GlobalVar.GVar['match_org_userId']:
        assert result['msg']=='该员工已认证为组织'
    else:
        assert re.search('该用户已经被授予这个角色|成功', str(result))


if __name__ == '__main__':
    pytest.main(['-sv', __file__])
