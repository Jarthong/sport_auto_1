__author__ = 'chenhh1334'
# -*- coding: utf-8 -*-

import pytest
import os
import requests
from db_fixture.login_token import *
from db_fixture.getdata import *

haggleId_effective = GetData(column='HAGGLE_ID',table='haggle_record').result()
haggleId =[0, None, haggleId_effective]
initiatorId_effective = GetData(column='INITIATOR_ID',table='haggle_record', where='WHERE HAGGLE_ID={HAGGLE_ID}'.format(HAGGLE_ID= haggleId_effective)).result()
initiatorId =['hhly***', None, initiatorId_effective]
total = GetData(column='count(*)-1',table='haggle_record',where="WHERE HAGGLE_ID={HAGGLE_ID} AND INITIATOR_ID ='{INITIATOR_ID}'".format(HAGGLE_ID= haggleId_effective,INITIATOR_ID=initiatorId_effective)).result()

@pytest.mark.parametrize('haggleId', haggleId)
@pytest.mark.parametrize('initiatorId', initiatorId)
@pytest.mark.parametrize('rows', [10,20,50])
def test_v1_user_guest_haggleUsers(login_c, haggleId, initiatorId, rows):
    """
    获取帮忙砍价用户列表(这个接口除了这4个参数外，其他参数没用，因此不用传)
    :param haggleId: 活动id
    :param initiatorId: 砍价发起人
    :param page: 页码
    :param rows: 行数
    """
    base_url = login_c.host + "/v1/user/_guest/haggleUsers"
    print(base_url)
    params = {'haggleId': haggleId,
              'initiatorId': initiatorId,
              'page': 1,
              'rows': rows}
    print("params:",params)
    r = requests.get(base_url, headers=login_c.headers, params=params, verify=False)
    result = r.json()
    print(result)
    if haggleId == None or initiatorId == None:
        assert '参数错误' in result['msg']

    elif haggleId == haggleId_effective and initiatorId == initiatorId_effective:
        assert result['msg'] == '成功'
        assert result['data']['total'] == total #判断接口砍价用户数量是否相等

    else:
        assert result['msg'] == '成功' and result['data']['total'] == 0



if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
