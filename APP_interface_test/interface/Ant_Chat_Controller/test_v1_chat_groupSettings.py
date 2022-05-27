__author__ = 'chenhh1334'
# -*- coding: utf-8 -*-

import pytest
import os
import requests
from db_fixture.login_token import *
from interface.Ant_Chat_Controller.data_fixture import Ant_Chat_Controller


roomId = [Ant_Chat_Controller().chat(column='ROOM_ID',table='chat_room_relation_group')[0], None]

@pytest.mark.parametrize('roomId', roomId)
def test_v1_chat_groupSettings(login_chh, roomId ):
    """
    群聊设置接口
    :param roomId: 聊天室id
    """
    base_url = login_chh[0] + "/v1/chat/groupSettings"
    params = {'roomId': roomId}
    r = requests.get(base_url, headers=login_chh[-1], params =params, verify=False)
    result = r.json()
    print(result)
    if roomId == None:
        assert result['result'] == '4002'
        assert '参数错误' in result['msg']
    else:
        assert result['result'] == '0'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
