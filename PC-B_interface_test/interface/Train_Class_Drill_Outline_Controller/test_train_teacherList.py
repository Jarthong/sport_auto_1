#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests
from db_fixture.common import *
from db_fixture.getdata import *

def test_teacherList(login_hq2):
    """
    分页获取教练信息
    :param public:
    :return:
    """
    base_url = login_hq2.host + "/train/teacher/teacherList"
    params = {}
    r = requests.get(base_url, headers=login_hq2.headers, verify=False, params=params)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))


