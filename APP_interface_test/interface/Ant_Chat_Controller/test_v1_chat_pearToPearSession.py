__author__ = 'chenhh1334'
# -*- coding: utf-8 -*-

import pytest
import os
import requests
from db_fixture.login_token import *
from interface.Ant_Chat_Controller.data_fixture import Ant_Chat_Controller

targetAntToken = [Ant_Chat_Controller().chat(column='ANT_TOKEN',table='user_token',where='limit 1,10')[0]]

@pytest.mark.parametrize('targetAntToken', targetAntToken)
def test_v1_chat_pearToPearSession(login_chh, targetAntToken ):
    """
    创建点对点会话
    :param targetAntToken: 目标触角token，长度为50
    """
    base_url = login_chh[0] + "/v1/chat/pearToPearSession"
    params = {'targetAntToken': targetAntToken}
    r = requests.post(base_url, headers=login_chh[-1], params =params, verify=False)
    result = r.json()
    print(result)
    assert result['result'] == '0'
    assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
