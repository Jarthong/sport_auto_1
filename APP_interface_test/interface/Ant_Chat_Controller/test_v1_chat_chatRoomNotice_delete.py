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
# noticeId = [Ant_Chat_Controller().chat(column='ID',table='chat_room_notice')[0], None]
#
# @pytest.mark.parametrize('noticeId', noticeId)
# def test_v1_chat_chatRoomNotice_delete(login, noticeId):
#     """ 删除聊天室公告 """
#     base_url = login[0] + "/v1/chat/chatRoomNotice"
#     params = {'noticeId': noticeId}
#     print("noticeId:", noticeId)
#     r = requests.delete(base_url, headers=login[-1], params=params, verify=False)
#     result = r.json()
#     print(result)
#     if noticeId != None:
#         assert result['result'] == '0' and result['msg'] == '成功'
#     else:
#         assert result['result'] == '4002'
#
# if __name__ == '__main__':
#     os.system('pytest -s -v {file}'.format(file=__file__))
