from db_fixture.common import GlobalVar

__author__ = 'huxm855'
import os

import pytest
import requests


@pytest.mark.parametrize('authOrgId', GlobalVar.GVar['authOrgIds']+[None])
def test_msg_authorizedmsg(login, authOrgId):
    ''' 查询授权消息'''
    base_url = login.host + "/msg/authorizedMsg"
    params = {'authOrgId': authOrgId}
    r = requests.get(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    if authOrgId is None:
        assert result['msg'] == '用户权限不足'
    else:
        assert result['msg'] == '成功'



if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
