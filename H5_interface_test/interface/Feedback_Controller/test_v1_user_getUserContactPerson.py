import pytest

from db_fixture.getdata import GetData

__author__ = 'huxm855'

import os

import requests

idd = [GetData('id', 'user_contact_person'), None]


@pytest.mark.parametrize('idd', idd)
def test_v1_user_getUserContactPerson(login, idd):
    ''' 获取联系人详细信息'''
    base_url = login.host + "/v1/user/getUserContactPerson"
    params = {'id': idd}
    r = requests.get(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    if idd is not None:
        assert result['msg'] == '成功'
    else:
        assert result['msg'] == '参数错误[Long@id]'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
