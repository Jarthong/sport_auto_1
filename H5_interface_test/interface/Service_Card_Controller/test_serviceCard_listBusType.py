#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os

from  db_fixture.login_token import *


def test_servicecard_listbustype(login):
    """
    获取状态列表
    :param public:
    :return:
    """
    base_url = login.host + "/v1/user/serviceCard/listBusType"
    params = {}
    r = requests.get(base_url, headers=login.headers, verify=False, params=params)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'
    assert '通用购买' in result['data'][1]['name']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
