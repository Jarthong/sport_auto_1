from interface.Shopping_Controller.data_fixture import Shopping_Controller

__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import re

import requests



def test_api_v1_shopping_list(login):
    ''' 购物车商品列表'''
    base_url =login[0] + "/v1/shopping/list"
    r = requests.get(base_url, headers=login[-1],verify=False)
    result = r.json()
    assert result['msg'] == '成功'
    for sku_code in Shopping_Controller().goods_shopping_cart():
        assert re.search(sku_code, str(result['data']))

if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
