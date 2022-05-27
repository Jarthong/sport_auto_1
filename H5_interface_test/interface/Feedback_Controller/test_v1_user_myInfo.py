from db_fixture.common import GlobalVar
from db_fixture.getdata import GetData

__author__ = 'huxm855'
import os

import requests


def test_v1_user_myInfo(login):
    ''' 获取我的信息'''
    base_url = login.host + "/v1/user/myInfo"
    r = requests.get(base_url, headers=login.headers, verify=False)
    result = r.json()
    userId, nickName, sex, authType = GetData(table='user_info', column='user_id,nick_name,sex,auth_type',
                                              where="where user_id='{user_id}'".format(
                                                  user_id=GlobalVar().GVar['user_id'])).result()
    print(result)
    assert result['msg'] == '成功'
    assert result['data']['userId'] == userId
    assert result['data']['nickName'] == nickName
    assert result['data']['sex'] == sex
    assert result['data']['authType'] == authType


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
