#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests
from db_fixture.getdata import *

def test_espn(login_hq3):
    """
    获取频道列表
    :param public:
    :return:
    """
    base_url = login_hq3.host + "/v1/guest/espn"
    params = {}
    r = requests.get(base_url, headers=login_hq3.headers, verify=False, params=params)
    result = r.json()
    print(result)
    a = result['data']
    a_list = [item[key] for item in a for key in item]
    print(a_list)
    if  result['msg'] == '成功':
        espn_result = GetData('espn_code','espn').results()
        assert list(espn_result)[0] in a_list

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))








