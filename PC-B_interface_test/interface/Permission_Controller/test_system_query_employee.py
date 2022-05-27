from db_fixture.common import GlobalVar

__author__ = 'huxm855'

import pytest
import requests


@pytest.mark.parametrize('authOrgId', GlobalVar.GVar['authOrgIds'])
def test_system_query_employee(login, authOrgId):
    ''' 查询组织员工 '''

    base_url = login.host + '/system/query/employee'
    params = {
        'page': 1,
        'rows': 15,
        'authOrgId': authOrgId
    }
    r = requests.get(base_url, headers=login.headers, params=params)
    result = r.json()
    assert result['result'] == '0'
    assert result['data']['total'] >= 1


if __name__ == '__main__':
    pytest.main(['-s', '-v', __file__])
