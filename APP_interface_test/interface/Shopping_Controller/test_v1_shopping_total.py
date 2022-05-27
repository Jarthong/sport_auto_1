from interface.Shopping_Controller.data_fixture import Shopping_Controller

__author__ = 'huxm855'
# -*- coding: utf-8 -*-

import os

import requests



def test_api_v1_shopping_total(login):
    ''' 根据 userid  获取购物车数量'''
    base_url =login[0] + "/v1/shopping/total"

    r = requests.get(base_url, headers=login[-1],verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'
    assert result['data']['total'] == Shopping_Controller().goods_shopping_cart(column='count(*)')[0]

# assert result['data']['total'] == Shopping_Controller().goods_shopping_cart(column='count(*)')[0]
#   E       assert 2 == 12
# test_v1_shopping_total.py:19: AssertionError
if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
