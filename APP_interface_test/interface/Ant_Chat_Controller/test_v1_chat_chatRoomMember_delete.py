# __author__ = 'chenhh1334'
# # -*- coding: utf-8 -*-
#
# import pytest
# import os
# import requests
# from db_fixture.login_token import *
# from test_interface.Ant_Chat_Controller.Sql_Conf import Ant_Chat_Controller
#
#
# roomId = [Ant_Chat_Controller().chat(column='ROOM_ID',table='chat_room_member')[0], None]
# userId = [Ant_Chat_Controller().chat(column='USER_ID',table='chat_room_member')[0], None]
#
# @pytest.mark.parametrize('roomId', roomId)
# @pytest.mark.parametrize('userId', userId)
# def test_v1_chat_chatRoomMember_delete(login, roomId, userId):
#     """ 退出群聊 """
#     base_url = login[0] + "/v1/chat/chatRoomMember"
#     params = {'roomId': roomId,
#               'userId': userId}
#     print("roomId:", roomId,"userId:", userId)
#     r = requests.delete(base_url, headers=login[-1], params=params, verify=False)
#     result = r.json()
#     print(result)
#     if roomId == None or userId ==None:
#         assert result['result'] == '4002'
#         assert '参数错误' in result['msg']
#     else:
#         assert result['result'] == '0'
#
#
# if __name__ == '__main__':
#     os.system('pytest -s -v {file}'.format(file=__file__))
