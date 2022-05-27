import os
import pytest
import requests
__author__ = 'huxm855'

from db_fixture.common import GlobalVar
from interface.Dict_Common_Controller.data_fixture import ReadMsgTotal

total = [ReadMsgTotal(),ReadMsgTotal(to_org_user_id=GlobalVar.GVar['train_org_userId'])]

@pytest.mark.parametrize('authOrgId,total', list(zip(GlobalVar.GVar['authOrgIds'],total)), ids=['match_org:','train_org:'])
def test_msg_unReadOrgMsgTotal(login, authOrgId, total):
    ''' 员工登录，查看组织未读消息总条数 '''

    base_url = login.host + '/msg/unReadOrgMsgTotal'
    params = { 'authOrgId': authOrgId}
    r = requests.get(base_url, headers=login.headers, params=params)
    result = r.json()
    print(result)
    assert  result['msg'] =='成功'
    assert  result['data'] ==total



if __name__ == '__main__':
    os.system('pytest -s -v test_msg_unReadOrgMsgTotal.py')

 