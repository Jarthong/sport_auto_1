import pytest

from db_fixture.getdata import GetData

__author__ = 'huxm855'
import os

import requests

from db_fixture.common import GlobalVar

@pytest.mark.parametrize('nickName', [
    GetData('nick_name', 'user_info', "where user_id='{user_id}'".format(user_id=GlobalVar.GVar['user_id'])).result(),
    None])
def test_v1_user_nickName_getUserInfo(login, nickName):
    ''' 根据用户昵称获取用户信息'''
    base_url = login.host + "/v1/user/nickName/getUserInfo"
    params = {'nickName': nickName}
    r = requests.get(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    if nickName is None:
        assert result['result'] == '4002'
    else:
        assert result['msg'] == '成功'
        assert result['data']['userId'] == GlobalVar.GVar['user_id']
        assert result['data']['nickName'] in nickName


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
