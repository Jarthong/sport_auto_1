__author__ = 'huxm855'

import os
import re

import pytest
import requests

from db_fixture.common import GlobalVar


@pytest.mark.parametrize('authOrgId', GlobalVar.GVar['authOrgIds'])
def test_system_getOrgRoleList(login, authOrgId):
    ''' 获取该组织下的角色列表 '''
    base_url = login.host + '/system/getOrgRoleList'
    params = {'authOrgId': authOrgId}
    r = requests.get(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    assert result['result'] == '0'
    print(result)
    if params['authOrgId'] == GlobalVar.GVar['match_org_userId']:
        re.search('赛事管理员', str(result))
    else:
        re.search('培训管理员', str(result))


if __name__ == '__main__':
    os.system('pytest -s -v test_system_getOrgRoleList.py')
