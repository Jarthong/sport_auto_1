__author__ = 'chenhh1334'
# -*- coding: utf-8 -*-

import pytest
import os
import requests
from db_fixture.login_token import *
from db_fixture.common import GlobalVar
from interface.Ant_Chat_Controller.data_fixture import Ant_Chat_Controller

roomId = Ant_Chat_Controller().chat_room_member(column='room_id')
userCardName = [None, '生活在滚滚红尘，总会遇到形形色色的人', '生活在滚滚红尘，总会遇到形形色色的人。我们改变不了别人']

@pytest.mark.parametrize('roomId', roomId)
@pytest.mark.parametrize('userCardName', userCardName)
def test_v1_chat_chatRoomMember_put(login,roomId, userCardName):
    """ 修改聊天室的名片，限制20个字符 """
    base_url = login[0] + "/v1/chat/chatRoomMember"
    params = {'roomId': roomId,
              'userCardName': userCardName,
              'userId': GlobalVar.GVar_chh['userid']}
    r = requests.put(base_url, headers=login[-1], data=params, verify=False)
    result = r.json()
    print(result)
    if userCardName == None:
        assert result['result'] == '4002'
        assert '参数错误[String@userCardName]' == result['msg']
    elif len(userCardName)> 20:
        assert result['result'] == '1000' and result['msg'] == '系统异常'
    else:
        assert result['data'] == True and result['result'] == '0'




if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
