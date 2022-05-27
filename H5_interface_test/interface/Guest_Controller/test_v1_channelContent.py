#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests
from db_fixture.getdata import *

espnCode = [GetData('espn_code','espn').result(),None]
@pytest.mark.parametrize('espnCode',espnCode)
def test_channelContent(login_hq3,espnCode):
    """
    获取频道内容列表
    :param public:
    :return:
    """
    base_url = login_hq3.host + "/v1/guest/channelContent"
    params = {
        'espnCode':espnCode,
        'page':1,
        'rows':15
    }
    r = requests.get(base_url, headers=login_hq3.headers, verify=False, params=params)
    result = r.json()
    print(result)
    if espnCode == None:    #本接口目前不作非空校验
        assert result['msg'] == '成功'
    else:
        assert result['msg'] == '成功'

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))







