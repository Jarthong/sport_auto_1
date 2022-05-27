#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests
from db_fixture.getdata import *


def test_tag(login_hq3):
    """
    获取标签列表
    :param public:
    :return:
    """
    base_url = login_hq3.host + "/v1/guest/tag"
    params = {}
    r = requests.get(base_url, headers=login_hq3.headers, verify=False, params=params)
    result = r.json()
    print(result)
    tagmsg = list(GetData('TAG_NAME','tag').results())
    print(tagmsg)
    assert tagmsg in result['data']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))











