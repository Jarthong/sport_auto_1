__author__ = 'chenhh1334'
# -*- coding: utf-8 -*-

import pytest
import os
import requests
from db_fixture.login_token import *
from db_fixture.getdata import *

haggleId_effective = GetData(column='ID',table='haggle_activity',where='where HAGGLE_STATUS= 1').result()
haggleId =[haggleId_effective, 0, None]
initiatorId_effective = GetData(column='INITIATOR_ID',table='haggle_initiator', where='where HAGGLE_ID={HAGGLE_ID}'.format(HAGGLE_ID= haggleId_effective)).result()
initiatorId =['hhly***', initiatorId_effective]
haggleUserId_effective = GetData(column='HAGGLE_USER_ID',table='haggle_record', where='where HAGGLE_ID={HAGGLE_ID}'.format(HAGGLE_ID= haggleId_effective)).result()
haggleUserId = ['hhly***', haggleUserId_effective]

@pytest.mark.parametrize('haggleId', haggleId)
@pytest.mark.parametrize('initiatorId', initiatorId)
@pytest.mark.parametrize('haggleUserId', haggleUserId)
def test_v1_user_guest_haggle(login_c, haggleId, initiatorId, haggleUserId):
    """
    获取砍价活动信息
    :param haggleId: 活动id
    :param initiatorId: 砍价发起人
    :param haggleUserId: 砍价人
    """
    base_url = login_c.host + "/v1/user/_guest/haggle"
    print(base_url)
    params = {'haggleId': haggleId,
              'initiatorId': initiatorId,
              'haggleUserId': haggleUserId}
    print("params:",params)
    r = requests.get(base_url, headers=login_c.headers, params=params, verify=False)
    result = r.json()
    print(result)
    if haggleId == None:
        assert result['result'] == '4002'
        assert '参数错误' in result['msg']

    elif haggleId == haggleId_effective and haggleUserId == GlobalVar.GVar_hq['c_user_id']:
        assert result['result'] == '0' and result['msg'] == '成功'
        assert result['data']['id'] == haggleId_effective #判断获取到活动信息的活动ID是否相同
        assert result['data']['currentUserHaggled'] == True #判断当前登录用户有没给这个活动砍过价，有就返回True

    elif haggleId == haggleId_effective and haggleUserId != GlobalVar.GVar_hq['c_user_id']:
        assert result['result'] == '0' and result['msg'] == '成功'
        assert result['data']['id'] == haggleId_effective #判断获取到活动信息的活动ID是否相同
        assert result['data']['currentUserHaggled'] == False #判断当前登录用户有没给这个活动砍过价，没有就返回False

    elif haggleId == 0:
        assert result['msg'] == '该砍价活动不存在'

    else:
        assert result['result'] == '0' and result['msg'] == '成功'

if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
