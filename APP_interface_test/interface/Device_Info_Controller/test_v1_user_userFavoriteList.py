from interface.Device_Info_Controller.data_fixture import GoodsVar, Device_Info_Controller

__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import pytest
import requests


favoriteType = range(1, 4)
rows = GoodsVar().rows

@pytest.mark.parametrize('favoriteType', favoriteType)
@pytest.mark.parametrize('rows', rows)
def test_v1_user_userFavoriteList(login, favoriteType, rows):
    ''' 用户收藏列表
    收藏类型(1：资讯，2：视频，3：商品)
    '''
    total = Device_Info_Controller().user_favorite(column='count(*)',other='and favorite_type =%d'%favoriteType)
    base_url = login[0] + "/v1/user/userFavoriteList"
    params = {'favoriteType': favoriteType, 'page': 1, 'rows': rows}
    r = requests.get(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    assert result['msg'] == '成功'
    assert result['data']['total'] == total[0]


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
