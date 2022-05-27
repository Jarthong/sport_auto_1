__author__ = 'huxm855'

import pytest
import requests

from db_fixture.common import GlobalVar, RandomVar
from interface.Permission_Controller.data_fixture import menu

rolelist = [510, 201]
authOrgId = GlobalVar.GVar['authOrgIds']


@pytest.mark.parametrize('rolelist,authOrgId', list(zip(rolelist, authOrgId)))
def test_system_createroleaccp(login, rolelist, authOrgId):
    ''' 创建职务分配角色授权服务接口'''
    base_url = login.host + '/system/createRoleAccp'
    rolelist = menu(ip_cate_id=rolelist)
    params = {
        'roleName': 'autotest 角色' + RandomVar().random_char_upper(),
        'roleType': 1,
        'authOrgId': authOrgId,
        'list': rolelist[0:RandomVar().random_num(1, len(rolelist))]
    }
    r = requests.post(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    assert result['result'] == '0'


if __name__ == '__main__':
    pytest.main(['-s', '-v', __file__])
