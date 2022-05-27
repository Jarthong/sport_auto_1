__author__ = 'chenhh1334'
# -*- coding: utf-8 -*-

import pytest
import os
import requests
from db_fixture.login_token import *
from db_fixture.common import GlobalVar
from db_fixture.getdata import *

@pytest.mark.parametrize('join', [1, 2, None, 5])
@pytest.mark.parametrize('rows', [10, 20, 50])
def test_v1_user_myHaggle(login_c, join, rows):
    """
    我的砍价
    :param join: 我参与的类型(1:我发起的砍价，2:我参与的砍价)
    :param page: 页码
    :param rows: 行数
    """
    base_url = login_c.host + "/v1/user/myHaggle"
    print(base_url)
    params = {'join': join,
              'page': 1,
              'rows': rows }
    print("params:",params)
    r = requests.get(base_url, headers=login_c.headers, params=params, verify=False)
    result = r.json()
    print(result)

    if join == None:
        assert '参数错误' in result['msg']

    elif join == 1: #我发起的砍价
        assert result['msg'] == '成功'
        assert result['data']['total'] == GetData(column='COUNT(*)', table='haggle_initiator', where= "where INITIATOR_ID='{INITIATOR_ID}'".format(INITIATOR_ID = GlobalVar.GVar_hq['c_user_id'])).result()

    elif join == 2 : #我参与的砍价
        assert result['msg'] == '成功'
        assert result['data']['total'] == GetData(column='COUNT(*)', table='haggle_record',where="where HAGGLE_USER_ID = '{HAGGLE_USER_ID}'".format(HAGGLE_USER_ID = GlobalVar.GVar_hq['c_user_id'])).result()

    else:
        assert result['result'] == '1000'
        assert '接口异常' in result['msg']



if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
