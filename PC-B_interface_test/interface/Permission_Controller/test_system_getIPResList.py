__author__ = 'huxm855'
import re

import pytest
import requests

from db_fixture.common import GlobalVar

type = [1, 2]
@pytest.mark.parametrize('authOrgId,type', list(zip(GlobalVar.GVar['authOrgIds'], type)))
def test_system_getipreslist(login, authOrgId, type):
    ''' 获取IP认证服务 '''
    params = {'authOrgId': authOrgId}
    base_url = login.host + '/system/getIPResList'
    r = requests.get(base_url, headers=login.headers, params=params)
    result = r.json()
    print(result)
    assert result['result'] == '0'
    if type == 1:
        re.search('赛事', str(result))
    else:
        re.search('班级', str(result))


if __name__ == '__main__':
    pytest.main(['-s', '-v', __file__])
