__author__ = 'chenhh1334'
# -*- coding: utf-8 -*-

import pytest
import os
from db_fixture.login_token import *
from db_fixture.getdata import *


voteId_effective = GetData(column='ID',table='vote_info').result()
voteId = [None,'MM', 0, voteId_effective]

@pytest.mark.parametrize('voteId', voteId)
def test_v1_vote_vote(login_c, voteId):
    """
    查看所有投票
    :param voteId: 投票id
    """
    base_url = login_c.host + "/v1/user/_guest/vote/voteList"
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
        assert result['msg'] == '成功' #无效Id返回成功，但无数据

    else:
        assert result['data']['id'] ==  voteId #返回该投票id下的所有投票信息




if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
