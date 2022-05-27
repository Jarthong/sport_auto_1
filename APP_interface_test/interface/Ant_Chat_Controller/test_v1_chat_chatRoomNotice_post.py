__author__ = 'chenhh1334'
# -*- coding: utf-8 -*-

import pytest
import os
import requests
from db_fixture.login_token import *
from interface.Ant_Chat_Controller.data_fixture import Ant_Chat_Controller


roomId = [Ant_Chat_Controller().chat(column='ROOM_ID',table='chat_room_notice')[0], None]
title = ['b'* 30, 'add聊天室公告']
content = ['bbbbbbbbbb'* 200, '您已经进入聊天室，请文明交流']
topNotice = ['true', 'false']

@pytest.mark.parametrize('roomId', roomId)
@pytest.mark.parametrize('title', title)
@pytest.mark.parametrize('content', content)
@pytest.mark.parametrize('topNotice', topNotice)

def test_v1_chat_chatRoomNotice_post(login_chh, roomId, title, content, topNotice):
    """
    新增聊天室公告
    :param roomId: 聊天室ID
    :param title: 公告标题，长度为25
    :param content: 公告内容，长度为1000
    :param topNotice: 公告是否置顶：Ture是，False否
    """
    base_url = login_chh[0] + "/v1/chat/chatRoomNotice"
    params = {'roomId':roomId,
              'title':title,
              'content':content,
              'topNotice':topNotice,}
    r = requests.post(base_url, headers=login_chh[-1], data =params, verify=False)
    result = r.json()
    print(params)
    print(result)
    if roomId == None or len(title)>25 or len(content)>1000 :
        assert result['result'] == '1000'
    else:
        assert result['result'] == '0'
        assert result['msg'] == '成功'

if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
