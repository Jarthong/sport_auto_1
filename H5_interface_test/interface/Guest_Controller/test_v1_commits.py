#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests
from db_fixture.getdata import *


IDS = (GetData('ID','info_collection').result())
counts = GetData('COMMIT_COUNT', 'info_collection', 'where ID = {ID}'.format(ID=IDS)).result()    #浏览数
pageId = [IDS,None,'^&*',999999999999]
@pytest.mark.parametrize('pageId',pageId)
def test_collection(login_hq3,pageId):
    """
    保存提交量
    info_collection = '信息搜集表'，"VIEW_COUNT"='访问量', "COMMIT_COUNT"='提交量',ID = page_id
    此接口有BUG需要修改，未作错误入参验证
    :param public:
    :return:
    """
    base_url = login_hq3.host + "/v1/guest/commits"
    params = {
        'pageId':pageId
    }
    print(params)
    r = requests.post(base_url, headers=login_hq3.headers, verify=False, params=params)
    result = r.json()
    print(result)
    if pageId is not None and pageId != '^&*' and pageId != '999999999999':
        assert result['msg'] == '成功'
    elif pageId == IDS:
        assert result['data'] == 1

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))









