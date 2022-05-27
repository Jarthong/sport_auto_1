__author__ = 'huxm855'
import os

import pytest
import requests

from db_fixture.common import GlobalVar


@pytest.mark.parametrize('userId', [None, GlobalVar.GVar_hxm['user_id'], 'hhly'])
def test_v1_ip_getUserServer(login, userId):
    ''' 根据userId获取服务'''
    base_url = login[0] + "/v1/ip/getUserServer"
    params = {'userId': userId}
    r = requests.get(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
