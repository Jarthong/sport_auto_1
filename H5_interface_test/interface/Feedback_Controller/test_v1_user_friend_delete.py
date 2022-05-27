import pytest

from db_fixture.common import GlobalVar
from db_fixture.getdata import GetData

__author__ = 'huxm855'

import os

import requests


@pytest.mark.parametrize('followUserId', [None, GetData('followed_user_id', 'user_follow',
                                                        "where user_id='{user_id}'".format(
                                                            user_id=GlobalVar.GVar['user_id'])).result()])
def test_v1_user_friend(login, followUserId):
    ''' 删除关注'''
    base_url = login.host + "/v1/user/friend"
    params = {'followUserId': followUserId}
    r = requests.delete(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    if followUserId == None:
        assert result['result'] == '4002'
    else:
        assert result['msg'] in ('取消关注失败', '成功')


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
