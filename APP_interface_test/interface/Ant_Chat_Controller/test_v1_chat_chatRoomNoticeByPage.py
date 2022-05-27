__author__ = 'chenhh1334'
# -*- coding: utf-8 -*-

import pytest
import os
import requests
from db_fixture.login_token import *
from interface.Ant_Chat_Controller.data_fixture import Ant_Chat_Controller


roomId = [Ant_Chat_Controller().chat(column='ROOM_ID',table='chat_room_notice')[0], None]

@pytest.mark.parametrize('roomId', roomId)
@pytest.mark.parametrize('rows', [10,20,50,100])

def test_v1_chat_chatRoomNoticeByPage(login_chh, roomId, rows ):
    """
    查询聊天室公告列表（分页）
    :param roomId: 聊天室ID
    :param rows: 每页显示的数量
    """
    base_url = login_chh[0] + "/v1/chat/chatRoomNoticeByPage"
    params = {'roomId': roomId,
              'page': 1,
              'rows': rows}
    r = requests.get(base_url, headers=login_chh[-1], params =params, verify=False)
    result = r.json()
    print(result)
    if roomId is not None:
        total = Ant_Chat_Controller().chat(column='count(*)', table='chat_room_notice',where='where room_id={room_id}'.format(room_id=roomId))[0]
        assert result['data']['total'] == total
        assert result['msg'] == '成功'
    else:
        assert result['msg'] == '参数错误[String@roomId]'

if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
