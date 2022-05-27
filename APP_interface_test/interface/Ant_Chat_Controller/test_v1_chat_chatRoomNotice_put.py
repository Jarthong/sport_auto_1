__author__ = 'chenhh1334'
# -*- coding: utf-8 -*-

import pytest
import os
import requests
from db_fixture.login_token import *
from interface.Ant_Chat_Controller.data_fixture import Ant_Chat_Controller


id = [Ant_Chat_Controller().chat(column='id',table='chat_room_notice')[0], None]
title = ['a'* 30, '欢迎加入大家庭']
content = ['aaaaaaaaaa'* 200, '内容：新成员请修改名片']
isTop = ['true', 'false']
isDelPic = ['Y', 'N']

@pytest.mark.parametrize('id', id)
@pytest.mark.parametrize('title', title)
@pytest.mark.parametrize('content', content)
@pytest.mark.parametrize('isTop', isTop)
@pytest.mark.parametrize('isDelPic', isDelPic)

def test_v1_chat_chatRoomNotice_put(login_chh, id, title, content, isTop, isDelPic):
    """
    修改聊天室公告
    :param id: 公告ID
    :param title: 公告标题，长度25
    :param content: 公告内容，长度1000
    :param isTop: 公告是否置顶：Ture是，False否
    :param isDelPic: 公告图片是否删除：Y是，N否
    """
    base_url = login_chh[0] + "/v1/chat/chatRoomNotice"
    params = {'id': id,
              'title':title,
              'content':content,
              'isTop':isTop,
              'isDelPic':isDelPic
              }
    r = requests.put(base_url, headers=login_chh[-1], data =params, verify=False)
    result = r.json()
    print(result)
    if id == None or len(title)>25 or len(content)>1000 :
        assert result['result'] == '1000' or result['result'] == '1005'
    else:
        assert result['result'] == '0'
        assert result['msg'] == '成功'

if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
