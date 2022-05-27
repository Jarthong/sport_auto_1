__author__ = 'huxm855'

import os

import pytest
import requests

from db_fixture.common import GlobalVar
from db_fixture.getdata import GetData

bizId, favoriteType = GetData('biz_id,favorite_type', 'user_favorite', "where user_id ='{user_id}'".format(
    user_id=GlobalVar.GVar['user_id'])).result()


@pytest.mark.skipif(favoriteType == 0, reason='无用户收藏数据，可删除')
def test_v1_user_userFavorite(login):
    ''' 删除用户收藏'''
    base_url = login.host + "/v1/user/userFavorite"
    params = {'bizId': bizId, 'favoriteType': favoriteType}
    r = requests.delete(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    assert result['result'] == '0'
    assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
