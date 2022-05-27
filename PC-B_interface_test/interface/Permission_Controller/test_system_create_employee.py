from interface.Permission_Controller.data_fixture import get_UnemployeeId, get_emplo_roleId

__author__ = 'huxm855'
import re

import pytest
import requests

from db_fixture.common import GlobalVar

group_user_id = GlobalVar().GVar['train_org_userId']
phone = [get_UnemployeeId(column='phone'), get_UnemployeeId(column='phone', auth_type=2),
         get_UnemployeeId(column='phone', group_user_id=GlobalVar().GVar['train_org_userId'])]
count = range(1, 4)
authOrgId = [GlobalVar.GVar['match_org_userId']] * 2 + [group_user_id]
roleId = [get_emplo_roleId(), get_emplo_roleId(),
          get_emplo_roleId(group_user_id=GlobalVar().GVar['train_org_userId'], ip_cate_id='201')]


@pytest.mark.parametrize('phone,count,authOrgId,roleId', list(zip(phone, count, authOrgId, roleId)))
def test_system_create_employee(login, phone, count, authOrgId, roleId):
    ''' 新建员工'''
    base_url = login.host + '/system/create/employee'
    params = {
        'phone': phone,
        'authOrgId': authOrgId,
        'roleId': roleId,
    }
    r = requests.post(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result, params)
    if count == 2:
        assert result['result'] == '5213'
        assert re.search('该员工已认证为组织', str(result))
    else:
        assert re.search('成功|组织人数超出上限', str(result))


if __name__ == '__main__':
    pytest.main(['-s', '-v', __file__])
