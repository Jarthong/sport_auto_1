__author__ = 'chenhh1334'
# -*- coding: utf-8 -*-

import pytest
import os
from db_fixture.login_token import *
from db_fixture.getdata import *
from db_fixture.common import GlobalVar

#有效的投票id
voteId_effective = GetData(column='ID',table='vote_info', where='where STATUS=0').result()
#某个投票的用户集
vote_users = GetData(column='user_id',table='vote_record',where='where vote_id = {vote_id}'.format(vote_id= voteId_effective)).results()

voteId = [None,'MM', 0, voteId_effective]
@pytest.mark.parametrize('voteId', voteId)
def test_v1_vote_userVote(login_c, voteId):
    """
    查看用户是否投票
    :param voteId: 投票id
    """
    base_url = login_c.host + "/v1/user/vote/userVote"
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

    elif GlobalVar.GVar_hq['c_user_id'] in vote_users:
        assert result['data']['isVoted'] ==  '1' #当前登录用户已经投过票

    else:
        assert result['data']['isVoted'] == '0'  # 当前登录用户没投过票



if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
