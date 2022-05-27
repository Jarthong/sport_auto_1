__author__ = 'huxm855'

import pytest
from db_fixture.common import GlobalVar
from db_fixture.getdata import GetData
import os

import requests


@pytest.mark.parametrize('rows', [10, 20, 50, 100])
@pytest.mark.parametrize('favoriteType', range(1, 4))
def test_v1_user_userFavoriteList(login, favoriteType, rows):
    ''' 用户收藏列表
    收藏类型(1：资讯，2：视频，3：商品)
    '''
    total = GetData('count(*)', 'user_favorite', "where user_id ='{user_id}' and favorite_type ={favorite_type}".format(
        user_id=GlobalVar.GVar['user_id'], favorite_type=favoriteType)).result()
    base_url = login.host + "/v1/user/userFavoriteList"
    params = {'favoriteType': favoriteType, 'page': 1, 'rows': rows}
    r = requests.get(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    assert result['msg'] == '成功'
    assert result['data']['total'] == total


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
