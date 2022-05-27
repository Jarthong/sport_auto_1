from db_fixture.getdata import GetData

from db_fixture.common import GlobalVar

__author__ = 'huxm855'

import os

import requests


def test_v1_user_contactWay(login):
    ''' 获取用户联系方式'''
    base_url = login.host + "/v1/user/contactWay"
    r = requests.get(base_url, headers=login.headers, verify=False)
    result = r.json()
    userId, userName = GetData('user_id,user_Name', 'user_info',
                               "where user_id='{user_id}'".format(user_id=GlobalVar.GVar['user_id'])).result()

    print(result)
    assert result['msg'] == '成功'
    assert result['data']['userId'] == userId
    assert result['data']['userName'] == userName


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
