__author__ = 'chenhh1334'
# -*- coding: utf-8 -*-

import pytest
import os
import requests
from db_fixture.login_token import *
from interface.Ant_Chat_Controller.data_fixture import Ant_Chat_Controller


noticeId = [Ant_Chat_Controller().chat(column='ID',table='chat_room_notice')[0], None]

@pytest.mark.parametrize('noticeId', noticeId)
def test_v1_chat_topChatRoomNotice(login_chh, noticeId ):
    """
    置顶聊天室公告
    :param noticeId: 公告ID
    """
    base_url = login_chh[0] + "/v1/chat/topChatRoomNotice"
    params = {'noticeId': noticeId}
    r = requests.put(base_url, headers=login_chh[-1], params =params, verify=False)
    print(params)
    result = r.json()
    print(result)
    if noticeId == None:
        assert result['result'] == '4002'
    else:
        assert result['result'] == '0' and result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
