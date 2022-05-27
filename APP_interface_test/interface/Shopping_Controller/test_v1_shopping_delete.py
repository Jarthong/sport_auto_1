__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import pytest
import requests
from interface.Shopping_Controller.data_fixture import Shopping_Controller

cart_id=[Shopping_Controller().goods_shopping_cart(column='id')[0:2],'456425']
@pytest.mark.parametrize('cart_id',cart_id)
def test_api_v1_shopping_delete(login,cart_id):
    ''' 根据 在购物车删除商品'''
    base_url =login[0] + "/v1/shopping/delete"
    params ={'ids':cart_id}
    r = requests.delete(base_url, headers=login[-1],params=params,verify=False)
    result = r.json()
    if cart_id=='456425':
        assert result['msg'] == '商品在数据库中不存在！'
    else:
        assert result['msg'] == '成功'
    #测试通过后，还原删除删除的购物车数据
    Shopping_Controller().init_goods_shopping_cart()

#  AssertionError: assert '只能修改或删除当前登录用户购物车中的商品！' == '成功'

if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
