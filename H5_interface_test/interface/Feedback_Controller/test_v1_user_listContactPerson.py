import pytest

from db_fixture.common import GlobalVar

__author__ = 'huxm855'

import os
import requests


@pytest.mark.parametrize('phone', [GlobalVar.GVar['user_phone'], '13628592308', None])
def test_v1_user_listContactPerson(login, phone):
    ''' 获取用户联系人列表'''
    base_url = login.host + "/v1/user/listContactPerson"
    params = {'phone': phone}
    r = requests.get(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
