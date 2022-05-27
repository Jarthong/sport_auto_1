__author__ = 'chenhh1334'
# -*- coding: utf-8 -*-

import pytest
import os
from db_fixture.login_token import *
from db_fixture.getdata import *


voteId_effective = GetData(column='ID',table='vote_info').result()
#某投票的总投票数
total_voteNum = GetData(column='count(1)',table='vote_record',where='where vote_id = {vote_id}'.format(vote_id=voteId_effective)).result()

voteId = [None,'MM', 0, voteId_effective]

@pytest.mark.parametrize('voteId', voteId)
@pytest.mark.parametrize('viewme', [0, 1])
def test_v1_vote_voteresult(login_c, voteId, viewme):
    """
    查看用户投票结果
    :param voteId: 投票id
    :param viewme: 是否查看自己的投票(0:不显示该用户已经投票的选择项, 1:显示该用户已经投票的选择项)
    """
    base_url = login_c.host + "/v1/user/vote/voteresult"
    print(base_url)
    params = {'voteId': voteId,
              'viewme':viewme}
    print("params:",params)
    r = requests.get(base_url, headers=login_c.headers, params=params, verify=False)
    result = r.json()
    print(result)
    if voteId == None :
        assert result['result'] == '4002' and '参数错误' in result['msg']

    elif voteId == 'MM':
        assert result['result'] == '2' and 'voteId不合法' in result['msg']

    elif voteId == 0:
        assert result['msg'] == '系统异常' #无效Id返回

    elif voteId == voteId_effective :
        assert result['data']['id'] ==  voteId #判断返回的投票id是否相等
        assert result['data']['questions'][0]['voteNum'] == total_voteNum #判断这个投票问题的投票量是否相等




if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
