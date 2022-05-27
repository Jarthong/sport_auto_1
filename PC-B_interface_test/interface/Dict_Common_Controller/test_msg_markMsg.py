from db_fixture.common import GlobalVar
from db_fixture.getdata import GetData

__author__ = 'huxm855'
import os

import pytest
import requests

authOrgIds = GlobalVar.GVar['authOrgIds'] + [None]


@pytest.mark.skipif(not GetData(
    sql='select id from msg_user_mapping where to_org_user_id in {to_org_user_id} and user_status=1 and  platform=2'.format(
        to_org_user_id=tuple(GlobalVar.GVar['authOrgIds']))).result(), reason='没有未读消息')
@pytest.mark.parametrize('authOrgId', authOrgIds)
def test_msg_markmsg(login, authOrgId):
    ''' 标记消息为已读'''
    base_url = login.host + "/msg/markMsg"
    msgId = GetData(
        sql='select id from msg_user_mapping where to_org_user_id=\'{to_org_user_id}\' and user_status=1 and  platform=2'.format(
            to_org_user_id=authOrgId)).result()
    params = {'msgIds': msgId, 'authOrgId': authOrgId}
    r = requests.post(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    if authOrgId is None:
        assert result['msg'] == '用户权限不足'
    else:
        assert result['msg'] == '成功'
        assert GetData(sql='select user_status from msg_user_mapping where id={msgId}'.format(
            msgId=msgId)).result() == 5  # 断言接口更新user_status 状态生效


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
