__author__ = 'huxm855'

import os
import requests
from db_fixture.common import GlobalVar
from interface.Dict_Common_Controller.data_fixture import ReadMsgTotal


def test_msg_unReadMsgTotal(login_match):
    ''' 组织登录，未读消息总条数 '''
    params = {'authOrgId': login_match.userId}
    base_url = login_match.host + '/msg/unReadMsgTotal'
    total = ReadMsgTotal(to_user_id=GlobalVar().GVar['match_org_userId'])
    r = requests.get(base_url, headers=login_match.headers, params=params)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'
    assert result['data'] == total


if __name__ == '__main__':

    os.system('pytest -s -v test_msg_unReadMsgTotal.py')
