__author__ = 'chenhh1334'
# -*- coding: utf-8 -*-

import pytest
import os
import requests
from db_fixture.login_token import *
from interface.Ant_Chat_Controller.data_fixture import Ant_Chat_Controller


roomId = [Ant_Chat_Controller().chat_room_member(column='room_id', user_id =GlobalVar.GVar_chh['userid']), None]
@pytest.mark.parametrize('roomId', roomId)
def test_v1_chat_chatRoomMember_get(login_chh, roomId):
    """ 查询聊天室成员是否在聊天室，存在返回聊天室成员对象，不存在不返回对象 """
    base_url = login_chh[0] + "/v1/chat/chatRoomMember"
    params = {'roomId': roomId }
    r = requests.get(base_url, headers=login_chh[-1], params = params, verify=False)
    result = r.json()
    print(result)
    if roomId != None:
        assert result["msg"] == "成功"
        assert result['data']['userId'] == GlobalVar.GVar_chh['userid']
    else:
        assert "参数错误" in result["msg"]
        assert result["result"] == '4002'



if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
