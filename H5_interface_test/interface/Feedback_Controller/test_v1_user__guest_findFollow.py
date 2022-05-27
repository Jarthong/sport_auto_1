import pytest

from db_fixture.common import GlobalVar

__author__ = 'huxm855'

import os

import requests



@pytest.mark.parametrize('rows', [10, 20, 50, 100])
@pytest.mark.parametrize('userId', ['None', GlobalVar.GVar['user_id'], 'hhly'])
def test_v1_user__guest_findFollow(login, rows, userId):
    ''' 我关注的人'''
    base_url = login.host + "/v1/user/_guest/findFollow"
    params = {'userId': userId, 'page': 1, 'rows': rows}
    r = requests.get(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'
    assert result['data']['total'] >= 0
    if result['data']['total'] > 0:
        assert result['data']['rows'] == rows


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
