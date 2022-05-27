import random

from db_fixture.common import GlobalVar
from db_fixture.getdata import GetData
from db_fixture.login_token import login_token

__author__ = 'huxm855'
import os
import pytest
import requests


@pytest.fixture(params=[GlobalVar.GVar['user_phone'], GlobalVar.GVar['match_org_phone'],
                        GlobalVar.GVar['train_org_phone2']])  # 分别员工,赛事组织，培训组织账号登录
def login(request):
    userInfo = login_token(phone=request.param)
    yield userInfo

    def tear_down_def():
        print(' ;ENDING')

    request.addfinalizer(tear_down_def)


def test_user_query_info(login):
    ''' 查询用户资料'''
    base_url = login.host + "/user/query/info"
    if login.userId == GlobalVar.GVar['user_id']:#为员工账号时,需要传authOrgId
        params = {'userId': login.userId, 'authOrgId':random.choice(GlobalVar.GVar['authOrgIds'])}#authOrgId为随机赛事或者培训组织账号
    else:
        params={'userId': login.userId,}
    r = requests.get(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    data=GetData('*','user_info',"user_id='{user_id}'".format(user_id=login.userId)).results_query()
    assert result['msg'] == '成功'
    assert result['data']['userId'] == data['USER_ID']
    assert result['data']['nickName'] == data['NICK_NAME']
    assert result['data']['account'] == data['ACCOUNT']
    assert result['data']['email'] == data['EMAIL']
    assert result['data']['status'] == data['STATUS']


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
