#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os

from  db_fixture.login_token import *

urllib3.disable_warnings(InsecureRequestWarning)


def test_servicecard_liststatus(login):
    """
    获取状态列表
    :param public:
    :return:
    """
    base_url = login.host + "/v1/user/_guest/serviceCard/listStatus"
    params = {}
    r = requests.get(base_url, headers=login.headers, verify=False, params=params)
    result = r.json()
    print(result)
    assert result['data'][1]['name'] == '未激活'
    assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
