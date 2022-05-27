__author__ = 'chenhh1334'
# -*- coding: utf-8 -*-

import pytest
import os
import requests
from db_fixture.login_token import *
from db_fixture.getdata import *

#有效的投票id
voteId_effective = GetData(column='ID',table='vote_info').result()
#查询该投票的详情
vote_Details = GetData(column='DETAILS_INTRO',table='vote_info',where='where ID = {ID}'.format(ID=voteId_effective)).result()

voteId = [None,'MM', 0, voteId_effective]

@pytest.mark.parametrize('voteId', voteId)
def test_v1_vote_voteDetails(login_c, voteId):
    """
    查看投票详情
    :param voteId: 投票id
    """
    base_url = login_c.host + "/v1/user/vote/voteDetails"
    print(base_url)
    params = {'voteId': voteId}
    print("params:",params)
    r = requests.get(base_url, headers=login_c.headers, params=params, verify=False)
    result = r.json()
    print(result)
    if voteId == None :
        assert result['result'] == '4002' and '参数错误' in result['msg']

    elif voteId == 'MM':
        assert result['result'] == '2' and 'voteId不合法' in result['msg']

    elif voteId == 0:
        assert result['msg'] == '接口异常（通用错误）' #无效Id返回接口异常

    else:
        assert result['msg'] == '成功'
        assert result['data']['voteDetail'] ==  vote_Details #判断返回的详情内容是否一致


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
