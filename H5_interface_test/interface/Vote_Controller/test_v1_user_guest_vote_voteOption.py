__author__ = 'chenhh1334'
# -*- coding: utf-8 -*-

import pytest
import os
import requests
from db_fixture.login_token import *
from db_fixture.getdata import *

optionId_effective = GetData(column='ID',table='vote_option').result()
optionId = [None,'MM', 0, optionId_effective]

@pytest.mark.parametrize('optionId', optionId)
def test_v1_vote_voteOption(login_c, optionId):
    """
    查看投票题目选项
    :param optionId: 选项id
    """
    base_url = login_c.host + "/v1/user/_guest/vote/voteOption"
    print(base_url)
    params = {'optionId': optionId}
    print("params:",params)
    r = requests.get(base_url, headers=login_c.headers, params=params, verify=False)
    result = r.json()
    print(result)
    if optionId==None:
        assert result['result'] == '4002' and '参数错误' in result['msg']
    elif optionId =='MM':
        assert '参数类型错误' in result['msg']
    elif optionId==0:
        assert result['msg'] == '成功' #无效optionId只返回成功，不返回数据
    else:
        assert result['msg'] == '成功' and result['data']['id'] ==  optionId #有效的optionId返回数据


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
