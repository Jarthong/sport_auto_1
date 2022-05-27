__author__ = 'chenhh1334'
# -*- coding: utf-8 -*-

import os

import pytest

from db_fixture.login_token import *
from interface.Ant_Chat_Controller.data_fixture import Ant_Chat_Controller

urllib3.disable_warnings(InsecureRequestWarning)

orgUserId = [Ant_Chat_Controller().org_info(column='org_user_id', user_id=GlobalVar.GVar_chh['userid']), None,
             'hhly0001']


# orgUserId = ['hhly91317']
@pytest.mark.parametrize('orgUserId', orgUserId)
def test_v1_chat_chatRoomMember_post(login_chh, orgUserId):
    """ 组织成员加入群聊 """
    base_url = login_chh[0] + "/v1/chat/chatRoomMember"
    params = {'orgUserId': orgUserId}
    r = requests.post(base_url, headers=login_chh[-1], data=params, verify=False)
    result = r.json()
    print(result)
    if orgUserId == None:
        assert result['result'] == '4002'
        assert '参数错误' in result['msg']

    elif orgUserId == 'hhly0001':
        assert result['result'] == '5324'
        assert result['msg'] == '无效的组织IP用户ID'

    else:
        assert result['result'] == '0'
        assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
