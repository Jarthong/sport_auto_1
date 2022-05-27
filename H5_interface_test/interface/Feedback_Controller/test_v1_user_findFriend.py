import os

import pytest

__author__ = 'huxm855'

import requests

from db_fixture.common import RandomVar


@pytest.mark.parametrize('rows', [10, 20, 50, 100])
def test_v1_user_findFriend(login, rows):
    ''' 我的通讯录'''
    base_url = login.host + "/v1/user/findFriend"
    params = {'keyword': RandomVar().random_char_upper(), 'page': 1, 'row': rows}
    r = requests.get(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
