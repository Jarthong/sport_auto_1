#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests
from db_fixture.common import *
from db_fixture.getdata import *


def test_teacher_info(login_hq2):
    """
    根据用户ID和组织ID获取教练信息
    :param public:
    :return:
    """
    base_url = login_hq2.host + "/train/teacher/info"
    params = {
        'userId':'seedp543681',
        'authOrgId':'seedp543681'
    }
    print(params)
    r = requests.get(base_url, headers=login_hq2.headers, verify=False, params=params)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))









