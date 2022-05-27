__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import requests
from db_fixture.common import GlobalVar
from interface.Goods_Controller.data_fixture import GoodsVar

rows = GoodsVar().rows


@pytest.mark.parametrize('rows', rows)
def test_v1_user__guest_findFans(login, rows):
    ''' 我的粉丝'''
    base_url = login[0] + "/v1/user/_guest/findFans"
    params = {'userId': GlobalVar.GVar_hxm['user_id'], 'page': 1, 'rows': rows}
    r = requests.get(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'
    assert result['data']['total'] >= 0
    if result['data']['total'] > 0:
        assert result['data']['rows'] == rows


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
