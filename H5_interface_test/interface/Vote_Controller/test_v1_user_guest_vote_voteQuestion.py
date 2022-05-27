__author__ = 'chenhh1334'
# -*- coding: utf-8 -*-

import pytest
import os
import requests
from db_fixture.login_token import *
from db_fixture.getdata import *

questionId_effective = GetData(column='ID',table='vote_question').result()
questionId = [None,'MM', 0, questionId_effective]

@pytest.mark.parametrize('questionId', questionId)
def test_v1_vote_voteQuestion(login_c, questionId):
    """
    查看投票题目
    :param questionId: 题目id
    """
    base_url = login_c.host + "/v1/user/_guest/vote/voteQuestion"
    print(base_url)
    params = {'questionId': questionId}
    print("params:",params)
    r = requests.get(base_url, headers=login_c.headers, params=params, verify=False)
    result = r.json()
    print(result)
    if questionId==None :
        assert result['result'] == '4002' and '参数错误' in result['msg']

    elif questionId == 'MM':
        assert '参数类型错误' in result['msg']

    elif questionId==0:
        assert result['msg'] == '成功' #无效questionId只返回成功，不返回数据

    else:
        assert result['msg'] == '成功' and result['data']['id'] ==  questionId #有效的questionId返回数据


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
