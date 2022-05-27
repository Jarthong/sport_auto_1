__author__ = 'chenhh1334'
# -*- coding: utf-8 -*-

import pytest
import os
import requests
from db_fixture.login_token import *
from interface.Ant_Chat_Controller.data_fixture import Ant_Chat_Controller


noticeId =  [Ant_Chat_Controller().chat(column='id', table='chat_room_notice'), None]

@pytest.mark.parametrize('noticeId', noticeId)
def test_v1_chat_chatRoomNotice_get(login_chh, noticeId):
    """
    查询聊天室公告
    :param noticeId: 公告ID
    """
    base_url = login_chh[0] + "/v1/chat/chatRoomNotice"
    params = {'noticeId': noticeId,}
    r = requests.get(base_url, headers=login_chh[-1], params =params, verify=False)
    result = r.json()
    print(result)
    if noticeId != None:
        assert result['result'] == '0' and result['msg'] == '成功'
    else:
        assert '参数错误' in result['msg']


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
