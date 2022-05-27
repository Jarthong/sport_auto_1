__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import requests
from db_fixture.common import RandomVar
from interface.Goods_Controller.data_fixture import GoodsVar


@pytest.mark.parametrize('rows', GoodsVar().rows)
def test_v1_user_findFriend(login, rows):
    ''' 我的通讯录'''
    base_url = login[0] + "/v1/user/findFriend"
    params = {'keyword': RandomVar.random_char_upper(5), 'page': 1, 'row': rows}
    r = requests.get(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
