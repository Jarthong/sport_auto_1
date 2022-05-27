from interface.Shopping_Controller.data_fixture import Shopping_Controller

__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import pytest
import requests

shopping_id=[Shopping_Controller().goods_shopping_cart(column='id')[0],None]
@pytest.mark.parametrize('shopping_id',[pytest.param(shopping_id[0],marks=pytest.mark.skipif(shopping_id[0]==0,reason='购物车无数据，跳过测试')),
                                    None
                                     ])
def test_api_v1_shopping_list(login,shopping_id):
    ''' 购物车商品列表'''
    base_url =login[0] + "/v1/shopping/modify"
    params= {'detailList[0].id':shopping_id,
             'detailList[0].num':1
             }
    r = requests.put(base_url, headers=login[-1],params=params,verify=False)
    result = r.json()
    if shopping_id :
        assert result['msg'] == '成功' or result['msg'] == '该商品已经下架'
    else:
        assert result['result'] == '20068'

# AssertionError: assert ('只能修改或删除当前登录用户购物车中的商品！' == '成功'

if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
