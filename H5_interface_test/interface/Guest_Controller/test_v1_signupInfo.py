#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests
from db_fixture.getdata import *


IDS = (GetData('ID','info_collection').result())
counts = GetData('view_count', 'info_collection', 'where ID = {ID}'.format(ID=IDS)).result()    #浏览数
pageId = [IDS,None,'^&*',999999999999]
@pytest.mark.parametrize('pageId',pageId)
def test_signupInfo(login_hq3,pageId):
    """
    获取活动报名信息
    :param public:
    :return:
    """
    base_url = login_hq3.host + "/v1/guest/singupInfo"
    params = {
        'pageId':pageId
    }
    print(params)
    r = requests.get(base_url, headers=login_hq3.headers, verify=False, params=params)
    result = r.json()
    print(result)
    if pageId == IDS:
        signup = GetData('title','info_collection','where ID = {ID}'.format(ID=IDS)).result()
        print(signup)
        assert result['msg'] == '成功'
        assert signup in  result['data']['title']
    elif pageId == None:
        assert '参数错误' in result['msg']

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))










