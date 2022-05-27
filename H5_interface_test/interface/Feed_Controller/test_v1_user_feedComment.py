__author__ = 'huxm855'

import os

import pytest
import requests

from db_fixture.common import GlobalVar


@pytest.mark.parametrize('userId', [None, GlobalVar.GVar['user_id'], 'hhly'])
@pytest.mark.parametrize('rows', [10, 20, 50, 100])
def test_v1_user_feedComment(login, userId, rows):
    ''' 获取个人中心我的评论功能接口'''
    base_url = login.host + "/v1/user/feedComment"
    params = {'userId': userId, 'page': 1, 'rows': rows}
    r = requests.get(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    if userId is None:
        assert result['msg'] == '参数错误[String@userId]'
    else:
        assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
